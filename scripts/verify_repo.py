from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    'README.md',
    'CONTRIBUTING.md',
    'CODE_OF_CONDUCT.md',
    'SECURITY.md',
    'GOVERNANCE.md',
    'VERSIONING.md',
    'CHANGELOG.md',
    'CODEOWNERS',
    'docs/methodology/continuous-improvement-loop.md',
    'docs/diagrams/README.md',
    'docs/loops/feature.md',
    'prompts/master-system-prompt.md',
    'prompts/chatgpt-web.md',
    'wiki/Home.md',
]

missing = [p for p in REQUIRED if not (ROOT / p).exists()]
if missing:
    print('Missing required files:')
    for item in missing:
        print(item)
    raise SystemExit(1)

markdown = list(ROOT.rglob('*.md'))
for path in markdown:
    text = path.read_text(encoding='utf-8')
    if not text.lstrip().startswith('#'):
        print('Markdown file without title:', path.relative_to(ROOT))
        raise SystemExit(1)

print('Repository structure OK')
print('Markdown files checked:', len(markdown))
