#!/usr/bin/env python3
"""Migrate legacy Inq module manifests and entry notes to unified inq.md files.

The legacy format kept module metadata in a per-module ``inq.toml`` and the
module document in a separate entry note.  Inq 0.4 keeps workspace-only
configuration in the root ``inq.toml`` and portable module metadata in YAML
frontmatter at the start of each module's ``inq.md``.

This script intentionally parses only the retired, small ``[module]`` schema.
It has no third-party dependencies and fails closed on unfamiliar input.
"""

from __future__ import annotations

import argparse
import ast
import json
import os
import re
import stat
import sys
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Iterable, Sequence


LEGACY_MANIFEST = "inq.toml"
LEGACY_ENTRY = "entry.md"
MODULE_DOCUMENT = "inq.md"
IGNORED_DIRECTORIES = {".git", "_inq"}
MARKDOWN_SUFFIXES = {".md", ".markdown"}

SECTION_RE = re.compile(r"^\s*\[([^]]+)]\s*$", re.MULTILINE)
ASSIGNMENT_RE = re.compile(r"^\s*([A-Za-z0-9_.-]+)\s*=", re.MULTILINE)
WIKILINK_RE = re.compile(r"(?P<open>!?\[\[)(?P<body>[^]\n]+)(?P<close>]])")
INLINE_LINK_RE = re.compile(
    r"(?P<open>!?\[[^]\n]*]\()"
    r"(?P<destination><[^>\n]+>|[^\s)\n]+)"
    r"(?P<title>\s+(?:\"[^\"\n]*\"|'[^'\n]*'|\([^()\n]*\)))?"
    r"(?P<close>\))"
)
REFERENCE_LINK_RE = re.compile(
    r"(?m)^(?P<open>[ \t]{0,3}\[[^]\n]+]:[ \t]*)"
    r"(?P<destination><[^>\n]+>|\S+)"
)


class MigrationError(RuntimeError):
    """A legacy file cannot be converted without guessing."""


@dataclass(frozen=True)
class LegacyModule:
    root: Path
    manifest: Path
    entry: Path
    name: str
    include: tuple[str, ...]
    note_selectors: tuple[str, ...]
    ambient_patterns: tuple[str, ...]


@dataclass(frozen=True)
class PendingWrite:
    path: Path
    content: str
    mode: int


def parse_args(argv: Sequence[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "workspace",
        nargs="?",
        type=Path,
        default=Path.cwd(),
        help="workspace root (default: current directory)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="validate and report the migration without changing files",
    )
    return parser.parse_args(argv)


def fail(path: Path, message: str) -> MigrationError:
    return MigrationError(f"{path}: {message}")


def parse_string(path: Path, key: str, value: str) -> str:
    try:
        parsed = ast.literal_eval(value)
    except (SyntaxError, ValueError) as error:
        raise fail(path, f"invalid {key} string: {error}") from error
    if not isinstance(parsed, str):
        raise fail(path, f"{key} must be a string")
    return parsed


def parse_string_array(path: Path, key: str, value: str) -> tuple[str, ...]:
    try:
        parsed = ast.literal_eval(value)
    except (SyntaxError, ValueError) as error:
        raise fail(path, f"invalid {key} array: {error}") from error
    if not isinstance(parsed, list) or not all(isinstance(item, str) for item in parsed):
        raise fail(path, f"{key} must be an array of strings")
    if len(parsed) != len(set(parsed)):
        raise fail(path, f"{key} contains duplicate selectors")
    return tuple(parsed)


def assignment_value(path: Path, source: str, key: str) -> str:
    match = re.search(rf"(?m)^\s*{re.escape(key)}\s*=\s*", source)
    if match is None:
        raise fail(path, f"missing module.{key}")

    start = match.end()
    if source[start : start + 1] != "[":
        return source[start : source.find("\n", start) if "\n" in source[start:] else len(source)].strip()

    quote: str | None = None
    escaped = False
    depth = 0
    for index in range(start, len(source)):
        character = source[index]
        if quote is not None:
            if escaped:
                escaped = False
            elif character == "\\":
                escaped = True
            elif character == quote:
                quote = None
            continue
        if character in {'"', "'"}:
            quote = character
        elif character == "[":
            depth += 1
        elif character == "]":
            depth -= 1
            if depth == 0:
                return source[start : index + 1].strip()
    raise fail(path, f"unterminated module.{key} array")


def classify_selectors(
    path: Path, selectors: Iterable[str]
) -> tuple[tuple[str, ...], tuple[str, ...]]:
    notes: list[str] = []
    ambient: list[str] = []

    def append_unique(items: list[str], value: str) -> None:
        if value not in items:
            items.append(value)

    for selector in selectors:
        if selector == "**":
            append_unique(notes, "./")
            append_unique(ambient, "**")
            continue

        suffix = PurePosixPath(selector).suffix.lower()
        if suffix in MARKDOWN_SUFFIXES:
            append_unique(notes, selector)
        elif suffix:
            append_unique(ambient, selector)
        else:
            raise fail(path, f"cannot classify legacy include selector {selector!r}")

    return tuple(notes), tuple(ambient)


def parse_legacy_manifest(path: Path) -> LegacyModule:
    source = path.read_text(encoding="utf-8")
    sections = SECTION_RE.findall(source)
    if sections != ["module"]:
        raise fail(path, f"expected only [module], found {sections!r}")
    keys = ASSIGNMENT_RE.findall(source)
    if sorted(keys) != ["entry", "include", "name"]:
        raise fail(path, f"expected name, entry, and include; found {keys!r}")

    name = parse_string(path, "name", assignment_value(path, source, "name"))
    entry_name = parse_string(path, "entry", assignment_value(path, source, "entry"))
    include = parse_string_array(path, "include", assignment_value(path, source, "include"))
    if entry_name != LEGACY_ENTRY:
        raise fail(path, f"unsupported entry note {entry_name!r}")
    if not include:
        raise fail(path, "module.include must not be empty")

    root = path.parent
    entry = root / entry_name
    if not entry.is_file():
        raise fail(path, f"entry note {entry_name!r} does not exist")
    output = root / MODULE_DOCUMENT
    if output.exists():
        raise fail(path, f"refusing to overwrite existing {MODULE_DOCUMENT}")

    notes, ambient = classify_selectors(path, include)
    return LegacyModule(root, path, entry, name, include, notes, ambient)


def walk_files(root: Path) -> Iterable[Path]:
    for current, directories, files in os.walk(root):
        directories[:] = sorted(
            directory for directory in directories if directory not in IGNORED_DIRECTORIES
        )
        current_path = Path(current)
        for filename in sorted(files):
            yield current_path / filename


def discover_modules(root: Path) -> list[LegacyModule]:
    modules: list[LegacyModule] = []
    for path in walk_files(root):
        if path.name != LEGACY_MANIFEST or path == root / LEGACY_MANIFEST:
            continue
        modules.append(parse_legacy_manifest(path))
    modules.sort(key=lambda module: module.root.relative_to(root).as_posix())
    return modules


def render_module_document(module: LegacyModule, body: str) -> str:
    lines = ["---", f"inq.module: {json.dumps(module.name, ensure_ascii=False)}"]
    if module.note_selectors:
        lines.append("inq.include:")
        lines.extend(f"  - {json.dumps(value, ensure_ascii=False)}" for value in module.note_selectors)
    if module.ambient_patterns:
        lines.append("inq.ambient:")
        lines.extend(f"  - {json.dumps(value, ensure_ascii=False)}" for value in module.ambient_patterns)
    lines.extend(["---", ""])
    return "\n".join(lines) + body


def normalized_candidate(path: PurePosixPath) -> str | None:
    parts: list[str] = []
    for part in path.parts:
        if part in {"", "."}:
            continue
        if part == "..":
            if not parts:
                return None
            parts.pop()
        else:
            parts.append(part)
    return "/".join(parts)


def destination_entry_path(
    destination: str,
    source: Path,
    workspace: Path,
    legacy_entries: set[str],
) -> str | None:
    destination = destination.removeprefix("/")
    if destination.startswith(("http://", "https://", "mailto:", "#")):
        return None

    path_part = re.split(r"[?#]", destination, maxsplit=1)[0]
    if not path_part:
        return None
    if not PurePosixPath(path_part).suffix:
        path_part += ".md"

    source_parent = PurePosixPath(source.relative_to(workspace).parent.as_posix())
    authored = PurePosixPath(path_part)
    candidates: list[PurePosixPath]
    if path_part.startswith(("./", "../")):
        candidates = [source_parent / authored]
    else:
        candidates = [authored, source_parent / authored]

    for candidate in candidates:
        normalized = normalized_candidate(candidate)
        if normalized in legacy_entries:
            return normalized
    return None


def rewrite_destination(
    destination: str,
    source: Path,
    workspace: Path,
    legacy_entries: set[str],
) -> tuple[str, bool]:
    bracketed = destination.startswith("<") and destination.endswith(">")
    raw = destination[1:-1] if bracketed else destination
    if destination_entry_path(raw, source, workspace, legacy_entries) is None:
        return destination, False

    match = re.match(r"(?P<path>[^?#]*)(?P<suffix>[?#].*)?$", raw)
    assert match is not None
    path = match.group("path")
    suffix = match.group("suffix") or ""
    if path.endswith("entry.md"):
        path = path[: -len("entry.md")] + MODULE_DOCUMENT
    elif path.endswith("entry"):
        path = path[: -len("entry")] + "inq"
    else:
        return destination, False
    rewritten = path + suffix
    return (f"<{rewritten}>" if bracketed else rewritten), True


def rewrite_links(
    source_text: str,
    source_path: Path,
    workspace: Path,
    legacy_entries: set[str],
) -> tuple[str, int]:
    changes = 0

    def wikilink(match: re.Match[str]) -> str:
        nonlocal changes
        body = match.group("body")
        destination, separator, label = body.partition("|")
        escaped_alias = bool(separator and destination.endswith("\\"))
        if escaped_alias:
            destination = destination[:-1]
        rewritten, changed = rewrite_destination(
            destination, source_path, workspace, legacy_entries
        )
        changes += int(changed)
        if changed and escaped_alias:
            # A backslash-escaped alias pipe is useful inside a Markdown table,
            # but Inq correctly treats that backslash as part of the target.
            # Keep the label as prose and retain an unaliased module link.
            return (
                label
                + " ("
                + match.group("open")
                + rewritten
                + match.group("close")
                + ")"
            )
        return (
            match.group("open")
            + rewritten
            + (separator + label if separator else "")
            + match.group("close")
        )

    def markdown_link(match: re.Match[str]) -> str:
        nonlocal changes
        rewritten, changed = rewrite_destination(
            match.group("destination"), source_path, workspace, legacy_entries
        )
        changes += int(changed)
        return (
            match.group("open")
            + rewritten
            + (match.groupdict().get("title") or "")
            + (match.groupdict().get("close") or "")
        )

    rewritten = WIKILINK_RE.sub(wikilink, source_text)
    rewritten = INLINE_LINK_RE.sub(markdown_link, rewritten)
    rewritten = REFERENCE_LINK_RE.sub(markdown_link, rewritten)
    return rewritten, changes


def atomic_write(write: PendingWrite) -> None:
    temporary = write.path.with_name(f".{write.path.name}.migration-tmp")
    if temporary.exists():
        raise fail(temporary, "stale migration temporary file exists")
    try:
        temporary.write_text(write.content, encoding="utf-8", newline="")
        temporary.chmod(stat.S_IMODE(write.mode))
        os.replace(temporary, write.path)
    finally:
        if temporary.exists():
            temporary.unlink()


def plan_migration(root: Path, modules: Sequence[LegacyModule]) -> tuple[list[PendingWrite], int]:
    legacy_entries = {
        module.entry.relative_to(root).as_posix()
        for module in modules
    }
    module_entries = {module.entry for module in modules}
    writes: list[PendingWrite] = []
    link_changes = 0

    for module in modules:
        body = module.entry.read_text(encoding="utf-8")
        document = render_module_document(module, body)
        document, changes = rewrite_links(document, module.root / MODULE_DOCUMENT, root, legacy_entries)
        link_changes += changes
        writes.append(
            PendingWrite(
                module.root / MODULE_DOCUMENT,
                document,
                module.entry.stat().st_mode,
            )
        )

    for path in walk_files(root):
        if path in module_entries or path.suffix.lower() not in MARKDOWN_SUFFIXES:
            continue
        source = path.read_text(encoding="utf-8")
        rewritten, changes = rewrite_links(source, path, root, legacy_entries)
        if changes:
            writes.append(PendingWrite(path, rewritten, path.stat().st_mode))
            link_changes += changes

    return writes, link_changes


def apply_migration(modules: Sequence[LegacyModule], writes: Sequence[PendingWrite]) -> None:
    for write in writes:
        atomic_write(write)
    for module in modules:
        module.entry.unlink()
        module.manifest.unlink()


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    root = args.workspace.resolve()
    workspace_manifest = root / LEGACY_MANIFEST
    if not workspace_manifest.is_file():
        raise fail(root, "workspace inq.toml does not exist")

    modules = discover_modules(root)
    if not modules:
        print("No legacy module manifests found.")
        return 0

    writes, link_changes = plan_migration(root, modules)
    ambient_modules = sum(1 for module in modules if module.ambient_patterns)
    markdown_only_modules = len(modules) - ambient_modules
    print(
        f"Validated {len(modules)} legacy modules "
        f"({ambient_modules} with ambient resources, "
        f"{markdown_only_modules} Markdown-only)."
    )
    print(f"Will rewrite {link_changes} link destination(s) in {len(writes)} file(s).")
    if args.dry_run:
        print("Dry run complete; no files changed.")
        return 0

    apply_migration(modules, writes)
    print(
        f"Created {len(modules)} inq.md documents and removed their legacy "
        "inq.toml + entry.md pairs."
    )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (MigrationError, OSError, UnicodeError) as error:
        print(f"error: {error}", file=sys.stderr)
        raise SystemExit(1)
