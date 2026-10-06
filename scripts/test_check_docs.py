"""Regression checks for bilingual document coverage, without writing fixtures."""

import os
import unittest
from pathlib import Path

import check_docs


class TranslationCoverageTests(unittest.TestCase):
    def setUp(self):
        paths, _, _ = check_docs.public_files()
        self.documents = {
            path.resolve(): check_docs.parse_markdown(path, path.read_text())[0]
            for path in paths
        }

    def add_document(self, name, counterpart):
        path = check_docs.REPO_ROOT / name
        target = check_docs.REPO_ROOT / counterpart
        link = Path(os.path.relpath(target, path.parent)).as_posix()
        self.documents[path] = check_docs.parse_markdown(path, f"[Other language]({link})")[0]

    def missing_counterparts(self):
        return {
            issue.path for issue in check_docs.check_translations(self.documents)
            if issue.rule == "translation-pair"
        }

    def test_english_only_document_is_rejected(self):
        for folder in ("docs", "examples"):
            with self.subTest(folder=folder):
                self.add_document(f"{folder}/en/probe.md", f"{folder}/probe.md")
                self.assertIn(f"{folder}/probe.md", self.missing_counterparts())

    def test_chinese_only_document_is_rejected(self):
        for folder in ("docs", "examples"):
            with self.subTest(folder=folder):
                self.add_document(f"{folder}/probe.md", f"{folder}/en/probe.md")
                self.assertIn(f"{folder}/en/probe.md", self.missing_counterparts())

    def test_complete_pair_is_accepted(self):
        self.add_document("docs/probe.md", "docs/en/probe.md")
        self.add_document("docs/en/probe.md", "docs/probe.md")
        self.assertEqual([], check_docs.check_translations(self.documents))

    def test_nested_orphans_are_rejected(self):
        self.add_document("docs/en/topic/probe.md", "docs/topic/probe.md")
        self.add_document("examples/topic/probe.md", "examples/en/topic/probe.md")
        self.assertEqual(
            {"docs/topic/probe.md", "examples/en/topic/probe.md"},
            self.missing_counterparts(),
        )

    def test_nested_complete_pair_is_accepted(self):
        self.add_document("docs/topic/probe.md", "docs/en/topic/probe.md")
        self.add_document("docs/en/topic/probe.md", "docs/topic/probe.md")
        self.assertEqual([], check_docs.check_translations(self.documents))

    def test_existing_special_pairs_are_accepted(self):
        self.assertEqual([], check_docs.check_translations(self.documents))

    def test_missing_language_switch_is_rejected(self):
        path = check_docs.REPO_ROOT / "docs/review.md"
        self.documents[path] = check_docs.parse_markdown(path, "# Review")[0]
        self.assertTrue(any(
            issue.rule == "language-switch" and issue.path == "docs/review.md"
            for issue in check_docs.check_translations(self.documents)
        ))


if __name__ == "__main__":
    unittest.main()
