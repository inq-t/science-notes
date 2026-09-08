"""Read-only link and internal reachability audit for named module directories.

This checks physical paths and Markdown openings, not mathematical truth or
Inq packaging semantics. Frozen records are opaque leaves of the active graph.
Fenced and inline code are excluded from link and math checks; math spans are
excluded from link checks. This is a scoped
Markdown check, not a full CommonMark or YAML parser; titles require editorial
review for agreement with their filenames.
"""

import argparse
import importlib.util
from pathlib import Path, PurePosixPath
import re

spec = importlib.util.spec_from_file_location("relocate", Path(__file__).with_name("relocate-notes.py"))
r = importlib.util.module_from_spec(spec)
spec.loader.exec_module(r)


def frozen(path):
    return bool(r.FROZEN.intersection(PurePosixPath(path).parts))


def frontmatter(text):
    """Return metadata, body and a malformed-frontmatter flag."""
    lines = text.lstrip("\ufeff").splitlines(keepends=True)
    if not lines or lines[0].strip() != "---":
        return "", "".join(lines).lstrip(), False
    for index, line in enumerate(lines[1:], 1):
        if line.strip() == "---":
            return "".join(lines[1:index]), "".join(lines[index + 1:]).lstrip(), False
    return "", "".join(lines), True


def prose(text):
    """Mask ordinary fenced/inline code while retaining prose line boundaries."""
    result = []
    fence = None
    for line in text.splitlines(keepends=True):
        match = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", line.rstrip("\r\n"))
        if fence:
            if match and match[1][0] == fence[0] and len(match[1]) >= len(fence) and not match[2].strip():
                fence = None
            result.append("\n")
        elif match and not (match[1][0] == "`" and "`" in match[2]):
            fence = match[1]
            result.append("\n")
        else:
            result.append(line)
    # Match paired runs of the same length; backticks within a longer run do
    # not terminate the span. Unpaired runs remain literal Markdown text.
    visible = re.sub(r"(?<!`)(`+)(?!`)[\s\S]*?(?<!`)\1(?!`)", "", "".join(result))
    return visible, fence is not None


def link_prose(text):
    """Math function notation such as [0](x) is not a Markdown link."""
    for pattern in (r"(?<!\\)\\\[[\s\S]*?(?<!\\)\\\]", r"(?<!\\)\\\([\s\S]*?(?<!\\)\\\)",
                    r"(?<!\\)\$\$[\s\S]*?(?<!\\)\$\$", r"(?<!\\)\$(?!\$)[^$]*?(?<!\\)\$"):
        text = re.sub(pattern, "", text)
    return text


def formatting(note, text):
    metadata, content, malformed = frontmatter(text)
    errors = []
    if malformed:
        errors.append("unclosed frontmatter")
    if PurePosixPath(note).name == "inq.md":
        keyword = re.search(r"(?m)^keywords:[ \t]*(.*)$", metadata)
        value = keyword[1].split(" #", 1)[0].strip() if keyword else ""
        following = metadata[keyword.end():] if keyword else ""
        has_list = bool(re.match(r"\s*-[ \t]+\S", following))
        if not keyword or (value in ("", "[]", "null", "~") and not has_list):
            errors.append("missing nonempty entrypoint keywords")
    lines = content.splitlines()
    if not lines or not lines[0].startswith("# ") or not lines[0][2:].strip():
        errors.append("missing first H1")
    else:
        after = next((line.strip() for line in lines[1:] if line.strip()), "")
        if not after or re.match(r"^(?:#|[-*+]\s|\d+[.)]\s|`{3,}|~{3,}|\||>|\\\[|\$\$|<)", after):
            errors.append("missing immediate prose summary")
    visible, unclosed_fence = prose(content)
    if unclosed_fence:
        errors.append("unclosed code fence")
    for opening, closing in ((r"\[", r"\]"), (r"\(", r"\)")):
        left_count = len(re.findall(r"(?<!\\)" + re.escape(opening), visible))
        right_count = len(re.findall(r"(?<!\\)" + re.escape(closing), visible))
        if left_count != right_count:
            errors.append(f"unbalanced {opening} delimiters")
    if len(re.findall(r"(?<!\\)\$\$", visible)) % 2:
        errors.append("unbalanced $$ delimiters")
    return visible, [(note, error) for error in errors]


def audit(root, module, files, resolver):
    prefix = module.rstrip("/") + "/"
    members = {p for p in files if p.startswith(prefix) and "__pycache__" not in PurePosixPath(p).parts}
    notes = {p for p in members if p.endswith((".md", ".markdown")) and not frozen(p)}
    edges = {}
    missing = []
    format_errors = []
    entry = prefix + "inq.md"
    if entry not in members:
        format_errors.append((entry, "missing module entrypoint"))
    for note in sorted(notes):
        text = (root / note).read_text(encoding="utf-8")
        visible, errors = formatting(note, text)
        format_errors.extend(errors)
        edges[note] = set()
        for target, wiki in r.links(link_prose(visible)):
            hit = resolver.resolve(note, target, wiki)
            if hit:
                edges[note].add(hit)
            elif target.strip() and not re.match(r"^(?:[a-zA-Z][a-zA-Z0-9+.-]*:|#|//)", target.strip()):
                missing.append((note, target))
    seen = set()
    stack = [entry]
    while stack:
        current = stack.pop()
        if current in seen:
            continue
        seen.add(current)
        stack.extend(p for p in edges.get(current, ()) if p.startswith(prefix))
    orphan_notes = sorted(notes - seen)
    orphan_resources = sorted(p for p in members - notes - seen if not frozen(p))
    return len(notes), len(members), orphan_notes, orphan_resources, missing, format_errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("modules", nargs="+")
    args = parser.parse_args()
    root = Path.cwd().resolve()
    files = r.inventory(root)
    resolver = r.Resolver(files)
    failures = 0
    for module in args.modules:
        module = module.rstrip("/")
        note_count, member_count, orphan_notes, orphan_resources, missing, format_errors = audit(root, module, files, resolver)
        print(f"{module}: {note_count} active notes; {member_count} files; {len(orphan_notes)} unreachable notes; {len(orphan_resources)} unlinked resources; {len(missing)} unresolved links; {len(format_errors)} format warnings")
        for label, rows in (("ORPHAN NOTE", orphan_notes), ("UNLINKED RESOURCE", orphan_resources), ("UNRESOLVED", missing), ("FORMAT", format_errors)):
            for row in rows:
                print(label, row)
        failures += len(orphan_notes) + len(orphan_resources) + len(missing) + len(format_errors)
    raise SystemExit(bool(failures))


if __name__ == "__main__":
    main()
