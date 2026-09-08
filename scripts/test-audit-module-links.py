"""Fixture tests for module closure and Markdown audit boundaries."""

import importlib.util
from pathlib import Path
import tempfile
import unittest

spec = importlib.util.spec_from_file_location("audit", Path(__file__).with_name("audit-module-links.py"))
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

ENTRY = "---\nkeywords: [test]\n---\n# Example\n\nA compact summary.\n\n"


class ModuleAuditTests(unittest.TestCase):
    def audit(self, files, module="sample"):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for name, content in files.items():
                path = root / name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(content, encoding="utf-8")
            return m.audit(root, module, set(files), m.r.Resolver(files))

    def test_transitive_note_and_resource_reachability(self):
        result = self.audit({
            "sample/inq.md": ENTRY + "[[support]]",
            "sample/support.markdown": "# Support\n\nA calculation.\n\n[Run](run.py) ![Plot](plot.svg)",
            "sample/run.py": "print('ok')",
            "sample/plot.svg": "<svg/>",
        })
        self.assertEqual(result, (2, 4, [], [], [], []))

    def test_external_detour_does_not_establish_internal_closure(self):
        result = self.audit({
            "sample/inq.md": ENTRY + "[[other/inq]]",
            "sample/orphan.md": "# Orphan\n\nA local thought.",
            "other/inq.md": ENTRY + "[[sample/orphan]]",
        })
        self.assertEqual(result[2], ["sample/orphan.md"])

    def test_nonexistent_and_missing_entry_modules_fail(self):
        self.assertIn(("sample/inq.md", "missing module entrypoint"), self.audit({})[5])
        result = self.audit({"sample/orphan.md": "# Orphan\n\nA local thought."})
        self.assertEqual(result[2], ["sample/orphan.md"])
        self.assertIn(("sample/inq.md", "missing module entrypoint"), result[5])

    def test_unlinked_code_is_not_hidden_by_frozen_records(self):
        result = self.audit({
            "sample/inq.md": ENTRY + "[[junk-drawer/history.md]]",
            "sample/run.py": "pass",
            "sample/junk-drawer/history.md": "Unformatted [[missing]] \\[",
        })
        self.assertEqual(result[3], ["sample/run.py"])
        self.assertEqual(result[4:], ([], []))

    def test_code_examples_are_not_links_or_math(self):
        content = ENTRY + "`[[missing]]` and ``x ` \\[ y``\n\n````md\n[[missing]]\n```\n\\[\n````\n~~~\n[[missing]]\n~~~\n"
        result = self.audit({"sample/inq.md": content})
        self.assertEqual(result[4:], ([], []))

    def test_unclosed_fence_and_real_math_error_are_reported(self):
        result = self.audit({"sample/inq.md": ENTRY + "\\[ x\n\n```py\n[[not-a-link]]"})
        self.assertEqual(result[4], [])
        self.assertIn(("sample/inq.md", "unclosed code fence"), result[5])
        self.assertIn(("sample/inq.md", "unbalanced \\[ delimiters"), result[5])

    def test_math_is_not_a_link_but_math_link_labels_remain_links(self):
        result = self.audit({
            "sample/inq.md": ENTRY + r"\(D[0](x)\) $D[0](x)$" + "\n$$\nD[0](x)\n$$\n" + r"\[D[0](x)\] [[support|The \(D[0](x)\) formula]]",
            "sample/support.md": "# Support\n\nA local thought.",
        })
        self.assertEqual(result, (2, 2, [], [], [], []))
        _, errors = m.formatting("sample/note.md", "# Example\n\nA summary.\n\n$$\nx")
        self.assertIn(("sample/note.md", "unbalanced $$ delimiters"), errors)

    def test_missing_or_empty_entry_keywords_fail(self):
        for metadata in ("", "---\nkeywords: []\n---\n", "---\nkeywords:\n---\n"):
            with self.subTest(metadata=metadata):
                _, errors = m.formatting("sample/inq.md", metadata + "# Example\n\nA summary.")
                self.assertIn(("sample/inq.md", "missing nonempty entrypoint keywords"), errors)
        _, errors = m.formatting("sample/inq.md", "---\nkeywords:\n  - test\n---\n# Example\n\nA summary.")
        self.assertEqual(errors, [])

    def test_malformed_frontmatter_and_nonprose_summary_fail(self):
        _, errors = m.formatting("sample/inq.md", "---\nkeywords: [test]\n# Example\n\nA summary.")
        self.assertIn(("sample/inq.md", "unclosed frontmatter"), errors)
        for summary in ("## Next section", "1. First item", "~~~py", "\\[x\\]", "> Quotation"):
            with self.subTest(summary=summary):
                _, errors = m.formatting("sample/note.md", "# Example\n\n" + summary)
                self.assertIn(("sample/note.md", "missing immediate prose summary"), errors)

    def test_real_missing_link_fails(self):
        result = self.audit({"sample/inq.md": ENTRY + "[[missing]] [Remote](https://example.com) [[#local]]"})
        self.assertEqual(result[4], [("sample/inq.md", "missing")])


if __name__ == "__main__":
    unittest.main()
