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
    '.github/PULL_REQUEST_TEMPLATE.md',
    '.github/workflows/ci-docs.yml',
    '.github/workflows/sync-wiki.yml',
    'docs/methodology/continuous-improvement-loop.md',
    'docs/methodology/definition-of-done.md',
    'docs/diagrams/README.md',
    'docs/loops/feature.md',
    'docs/loops/bugfix-loop.md',
    'docs/loops/release.md',
    'docs/verifiers/README.md',
    'prompts/master-system-prompt.md',
    'prompts/chatgpt-web.md',
    'prompts/continuous-improvement.md',
    'wiki/Home.md',
    'wiki/Loops.md',
    'wiki/Prompts.md',
    'wiki/Releases.md',
    'wiki/Verifiers.md',
]

REQUIRED_MERMAID = [
    'docs/methodology/continuous-improvement-loop.md',
    'docs/methodology/definition-of-done.md',
    'docs/diagrams/README.md',
    'docs/loops/feature.md',
    'docs/loops/release.md',
    'wiki/Home.md',
]


def fail(title, items):
    if items:
        print(title)
        for item in items:
            print('-', item)
        raise SystemExit(1)


missing = [p for p in REQUIRED if not (ROOT / p).exists()]
fail('Missing required files:', missing)

markdown = list(ROOT.rglob('*.md'))
without_title = []
for path in markdown:
    text = path.read_text(encoding='utf-8')
    if not text.lstrip().startswith('#'):
        without_title.append(str(path.relative_to(ROOT)))
fail('Markdown files without title:', without_title)

without_mermaid = []
for p in REQUIRED_MERMAID:
    if '```mermaid' not in (ROOT / p).read_text(encoding='utf-8'):
        without_mermaid.append(p)
fail('Required diagram docs without Mermaid:', without_mermaid)

print('Repository structure OK')
print('Required files checked:', len(REQUIRED))
print('Markdown files checked:', len(markdown))
