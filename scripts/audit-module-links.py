"""Read-only link and internal reachability audit for named module directories.

This checks physical paths and Markdown openings, not mathematical truth or
Inq packaging semantics. Frozen records are opaque leaves of the active graph.
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


def body(text):
    if text.startswith("---\n") or text.startswith("---\r\n"):
        return re.split(r"(?m)^---\s*$", text, maxsplit=2)[-1].lstrip()
    return text.lstrip()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("modules", nargs="+")
    args = parser.parse_args()
    root = Path.cwd().resolve()
    files = r.inventory(root)
    resolver = r.Resolver(files)
    failures = 0
    for module in args.modules:
        prefix = module.rstrip("/") + "/"
        members = {p for p in files if p.startswith(prefix) and "__pycache__" not in p}
        notes = {p for p in members if p.endswith(".md") and not frozen(p)}
        edges = {}
        missing = []
        format_errors = []
        for note in sorted(notes):
            text = (root / note).read_text(encoding="utf-8")
            edges[note] = set()
            for target, wiki in r.links(text):
                hit = resolver.resolve(note, target, wiki)
                if hit:
                    edges[note].add(hit)
                elif target.strip() and not re.match(r"^(?:[a-zA-Z][a-zA-Z0-9+.-]*:|#|//)", target.strip()):
                    missing.append((note, target))
            lines = body(text).splitlines()
            if not lines or not lines[0].startswith("# "):
                format_errors.append((note, "missing first H1"))
            else:
                after = next((line for line in lines[1:] if line.strip()), "")
                if not after or after.startswith(("#", "- ", "* ", "```", "|")):
                    format_errors.append((note, "missing immediate prose summary"))
            for opening, closing in ((r"\[", r"\]"), (r"\(", r"\)")):
                left_count = len(re.findall(r"(?<!\\)" + re.escape(opening), text))
                right_count = len(re.findall(r"(?<!\\)" + re.escape(closing), text))
                if left_count != right_count:
                    format_errors.append((note, f"unbalanced {opening} delimiters"))
        seen = set()
        stack = [prefix + "inq.md"]
        while stack:
            current = stack.pop()
            if current in seen:
                continue
            seen.add(current)
            stack.extend(p for p in edges.get(current, ()) if p.startswith(prefix))
        orphan_notes = sorted(notes - seen)
        orphan_resources = sorted(p for p in members - seen if not p.endswith(".md") and not frozen(p))
        print(f"{module}: {len(notes)} active notes; {len(members)} files; {len(orphan_notes)} unreachable notes; {len(orphan_resources)} unlinked resources; {len(missing)} unresolved links; {len(format_errors)} opening/math warnings")
        for label, rows in (("ORPHAN NOTE", orphan_notes), ("UNLINKED RESOURCE", orphan_resources), ("UNRESOLVED", missing), ("FORMAT", format_errors)):
            for row in rows:
                print(label, row)
        failures += len(orphan_notes) + len(orphan_resources) + len(missing) + len(format_errors)
    raise SystemExit(bool(failures))


if __name__ == "__main__":
    main()
