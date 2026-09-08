"""Read-only unit tests for link rebasing; no workspace edits."""

import importlib.util
from pathlib import Path
import unittest

spec = importlib.util.spec_from_file_location("relocate", Path(__file__).with_name("relocate-notes.py"))
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


class RelocationTests(unittest.TestCase):
    def setUp(self):
        self.files = {"old/a.md", "old/b.md", "old/receipts/r.py", "else/a.md", "outside/c.md"}
        self.moves = {"old/a.md": "new/a.md", "old/receipts/r.py": "new/receipts/r.py"}
        self.resolver = m.Resolver(self.files)

    def change(self, text, source="old/a.md", destination="new/a.md"):
        return m.rewrite(text, source, destination, self.moves, self.resolver)[0]

    def test_local_outgoing_and_anchor(self):
        self.assertEqual(self.change("[[b#Claim|proof]]"), "[[old/b#Claim|proof]]")

    def test_moved_receipt(self):
        self.assertEqual(self.change("[[receipts/r.py|run]]"), "[[new/receipts/r.py|run]]")

    def test_incoming(self):
        self.assertEqual(self.change("[[old/a|A]]", "outside/c.md", "outside/c.md"), "[[new/a|A]]")

    def test_markdown(self):
        self.assertEqual(self.change("[proof](b.md#Q)"), "[proof](../old/b.md#Q)")

    def test_reference(self):
        self.assertEqual(self.change("[p]: b.md#Q"), "[p]: ../old/b.md#Q")

    def test_multiline_label(self):
        self.assertEqual(self.change("[[b|a long\nlabel]]"), "[[old/b|a long\nlabel]]")

    def test_unresolved_and_remote_unchanged(self):
        value = "[[missing]] [web](https://example.com) [[#here]]"
        self.assertEqual(self.change(value), value)

    def test_ambiguous_suffix(self):
        self.assertIsNone(self.resolver.resolve("outside/c.md", "a"))

    def test_extensions_preserved(self):
        self.assertEqual(self.change("[[old/a.md]]"), "[[new/a.md]]")

    def test_directory_escape(self):
        with self.assertRaises(ValueError):
            m.safe_path(Path.cwd().resolve(), "../outside.md")


if __name__ == "__main__":
    unittest.main()
