from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_required_files_exist():
    required = [
        'README.md',
        'CONTRIBUTING.md',
        'SECURITY.md',
        'GOVERNANCE.md',
        'VERSIONING.md',
        'docs/methodology/continuous-improvement-loop.md',
        'docs/loops/feature.md',
        'prompts/master-system-prompt.md',
    ]
    missing = [p for p in required if not (ROOT / p).exists()]
    assert not missing


def test_markdown_files_have_titles():
    for path in ROOT.rglob('*.md'):
        assert path.read_text(encoding='utf-8').lstrip().startswith('#'), path
