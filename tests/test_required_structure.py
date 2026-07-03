import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class RequiredStructureTests(unittest.TestCase):
    def test_required_files_exist(self):
        required = [
            'README.md',
            'CONTRIBUTING.md',
            'SECURITY.md',
            'GOVERNANCE.md',
            'VERSIONING.md',
            'docs/methodology/continuous-improvement-loop.md',
            'docs/loops/feature.md',
            'prompts/master-system-prompt.md',
            'wiki/Home.md',
        ]
        missing = [p for p in required if not (ROOT / p).exists()]
        self.assertEqual([], missing)

    def test_markdown_files_have_titles(self):
        for path in ROOT.rglob('*.md'):
            text = path.read_text(encoding='utf-8')
            self.assertTrue(text.lstrip().startswith('#'), str(path.relative_to(ROOT)))

    def test_key_docs_have_mermaid(self):
        required = [
            'docs/methodology/continuous-improvement-loop.md',
            'docs/diagrams/README.md',
            'docs/loops/feature.md',
            'wiki/Home.md',
        ]
        missing = [p for p in required if '```mermaid' not in (ROOT / p).read_text(encoding='utf-8')]
        self.assertEqual([], missing)


if __name__ == '__main__':
    unittest.main()
