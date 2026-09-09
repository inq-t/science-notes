"""Plan and apply explicit, link-aware relocations within this Git workspace.

No source text is rewritten except link destinations. Raw records are frozen.
The manifest names every move; no directory is recursively removed. Apply is
opt-in, refuses occupied destinations and protects pre-existing dirty files.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import posixpath
import re
import subprocess
from urllib.parse import unquote

WIKI = re.compile(r"(?P<left>!?\[\[)(?P<body>[^\]]+)(?P<right>\]\])")
INLINE = re.compile(r"(?P<left>!?\[[^\]\n]*\]\()(?P<dest><[^>\n]+>|[^\s)]+)(?P<tail>[^)\n]*\))")
REFERENCE = re.compile(r"(?m)^(?P<left>[ \t]{0,3}\[[^\]\n]+\]:[ \t]*)(?P<dest><[^>\n]+>|\S+)")
FROZEN = {"inbox", "chats", "junk-drawer", "deep-research", "research-runs"}


def git(root, *args):
    return subprocess.check_output(["git", *args], cwd=root).decode("utf-8")


def inventory(root):
    names = git(root, "ls-files", "-z") + git(root, "ls-files", "--others", "--exclude-standard", "-z")
    return {name for name in names.split("\0") if name and (root / name).is_file()}


def safe_path(root, name):
    if "\\" in name or PurePosixPath(name).is_absolute() or ".." in PurePosixPath(name).parts:
        raise ValueError(f"Expected workspace-relative path: {name}")
    path = (root / name).resolve()
    if path == root or not path.is_relative_to(root):
        raise ValueError(f"Path escapes workspace: {name}")
    return path


class Resolver:
    def __init__(self, files):
        self.files = set(files)
        self.suffixes = {}
        for file in files:
            parts = file.split("/")
            for start in range(len(parts)):
                self.suffixes.setdefault("/".join(parts[start:]), set()).add(file)

    def resolve(self, source, target, wiki=True):
        target = unquote(target.strip()).replace("\\", "/")
        if not target or target.startswith(("#", "//")) or re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target):
            return None
        suffixes = [target]
        if not PurePosixPath(target).suffix:
            suffixes += [target + ".md", target + ".markdown"]
        candidates = []
        for name in suffixes:
            relative = posixpath.normpath(posixpath.join(posixpath.dirname(source), name))
            candidates.extend([name, relative] if wiki and "/" in target and not target.startswith(".") else [relative, name])
        for candidate in candidates:
            if candidate in self.files:
                return candidate
        if wiki:
            hits = set().union(*(self.suffixes.get(name, set()) for name in suffixes))
            if len(hits) == 1:
                return hits.pop()
        return None


def split_anchor(target):
    before, sep, after = target.partition("#")
    return before, sep + after if sep else ""


def rewrite(text, source, destination, moves, resolver):
    changes = []

    def convert(raw, wiki):
        angle = raw.startswith("<") and raw.endswith(">")
        value = raw[1:-1] if angle else raw
        target, anchor = split_anchor(value)
        resolved = resolver.resolve(source, target, wiki)
        if resolved is None or (resolved not in moves and source == destination):
            return raw
        final = moves.get(resolved, resolved)
        if wiki:
            result = final[:-3] if final.endswith(".md") and not target.endswith(".md") else final
        else:
            result = posixpath.relpath(final, posixpath.dirname(destination) or ".")
        result += anchor
        if angle or (not wiki and " " in result):
            result = "<" + result + ">"
        if result != raw:
            changes.append((raw, result))
        return result

    def wiki_match(match):
        target, pipe, label = match["body"].partition("|")
        return match["left"] + convert(target, True) + (pipe + label if pipe else "") + match["right"]

    text = WIKI.sub(wiki_match, text)
    text = INLINE.sub(lambda m: m["left"] + convert(m["dest"], False) + m["tail"], text)
    text = REFERENCE.sub(lambda m: m["left"] + convert(m["dest"], False), text)
    return text, changes


def links(text):
    for match in WIKI.finditer(text):
        yield split_anchor(match["body"].partition("|")[0])[0], True
    for pattern in (INLINE, REFERENCE):
        for match in pattern.finditer(text):
            yield split_anchor(match["dest"].strip("<>"))[0], False


def digest(data):
    return hashlib.sha256(data).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    root = Path.cwd().resolve()
    spec = json.loads(args.manifest.read_text(encoding="utf-8"))
    moves = spec["moves"]
    frozen_prefixes = tuple(name.rstrip("/") + "/" for name in spec.get("frozen_prefixes", []))
    for prefix in frozen_prefixes:
        safe_path(root, prefix.rstrip("/"))
    receipt_path = args.manifest.with_suffix(".receipt.json")
    if args.apply and receipt_path.exists():
        raise ValueError(f"Receipt would overwrite an earlier run: {receipt_path}")
    if len(set(moves.values())) != len(moves):
        raise ValueError("Duplicate destination")
    files = inventory(root)
    resolver = Resolver(files)
    protected = set(spec.get("protected", []))
    for source, dest in moves.items():
        src, dst = safe_path(root, source), safe_path(root, dest)
        if source.startswith(frozen_prefixes):
            raise ValueError(f"Move frozen record only under a separate reviewed operation: {source}")
        if not src.is_file() or dst.exists() or source in protected:
            raise ValueError(f"Missing source, occupied target or protected move: {source} -> {dest}")
    pending = {}
    changed_links = 0
    frozen = {}
    for source in sorted(files):
        if not source.endswith((".md", ".markdown")):
            continue
        data = (root / source).read_bytes()
        if FROZEN.intersection(PurePosixPath(source).parts) or source.startswith(frozen_prefixes):
            if source in moves:
                raise ValueError(f"Move frozen record only under a separate reviewed operation: {source}")
            frozen[source] = digest(data)
            continue
        destination = moves.get(source, source)
        text = data.decode("utf-8")
        updated, changes = rewrite(text, source, destination, moves, resolver)
        if changes and source in protected:
            raise ValueError(f"Protected file needs a link update: {source}")
        if source in moves or changes:
            pending[source] = updated.encode("utf-8")
        changed_links += len(changes)
    print(f"{len(moves)} explicit moves; {len(pending)} Markdown destinations; {changed_links} link updates; {len(frozen)} frozen records")
    if not args.apply:
        print("Dry run: no files changed.")
        return
    receipt = {"manifest": args.manifest.as_posix(), "moves": [], "link_updates": changed_links,
               "frozen_prefixes": list(frozen_prefixes)}
    for source, dest in moves.items():
        src, dst = safe_path(root, source), safe_path(root, dest)
        data = src.read_bytes()
        dst.parent.mkdir(parents=True, exist_ok=True)
        # Exact targets were validated above. Rename is confined to this workspace.
        src.rename(dst)
        receipt["moves"].append({"from": source, "to": dest, "before_sha256": digest(data)})
    for source, data in pending.items():
        safe_path(root, moves.get(source, source)).write_bytes(data)
    for source, expected in frozen.items():
        if digest((root / source).read_bytes()) != expected:
            raise ValueError(f"Frozen record changed: {source}")
    receipt["frozen_records_verified"] = len(frozen)
    for row in receipt["moves"]:
        row["after_sha256"] = digest((root / row["to"]).read_bytes())
    receipt_path.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(f"Applied; provenance: {receipt_path}")


if __name__ == "__main__":
    main()
