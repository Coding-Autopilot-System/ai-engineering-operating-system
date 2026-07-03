from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    'README.md',
    'LICENSE',
    'CONTRIBUTING.md',
    'CODE_OF_CONDUCT.md',
    'SECURITY.md',
    'GOVERNANCE.md',
    'VERSIONING.md',
    'CHANGELOG.md',
    'CODEOWNERS',
    'AGENTS.md',
    '.github/PULL_REQUEST_TEMPLATE.md',
    '.github/copilot-instructions.md',
    '.github/workflows/ci-docs.yml',
    '.github/workflows/sync-wiki.yml',
    'docs/README.md',
    'docs/methodology/quickstart.md',
    'docs/methodology/glossary.md',
    'docs/methodology/anti-patterns.md',
    'docs/methodology/continuous-improvement-loop.md',
    'docs/methodology/definition-of-done.md',
    'docs/methodology/maturity-model.md',
    'docs/diagrams/README.md',
    'docs/loops/README.md',
    'docs/loops/feature.md',
    'docs/loops/bugfix-loop.md',
    'docs/loops/refactoring.md',
    'docs/loops/pipeline-repair.md',
    'docs/loops/iac.md',
    'docs/loops/security.md',
    'docs/loops/performance.md',
    'docs/loops/release.md',
    'docs/verifiers/README.md',
    'docs/evaluations/README.md',
    'docs/local-runner/README.md',
    'docs/showcase/README.md',
    'docs/adoption/README.md',
    'docs/operations/README.md',
    'docs/architecture/context-loading.md',
    'docs/architecture/context-engineering.md',
    'docs/prompts/quality.md',
    'docs/quality-system/README.md',
    'templates/README.md',
    'templates/complete-project-context.md',
    'templates/repository-context-template.md',
    'templates/agent-instructions-template.md',
    'prompts/README.md',
    'prompts/master-system-prompt.md',
    'prompts/chatgpt-web.md',
    'prompts/continuous-improvement.md',
    'wiki/Home.md',
    'wiki/Architecture-Guide.md',
    'wiki/Loops.md',
    'wiki/Prompts.md',
    'wiki/Releases.md',
    'wiki/Verifiers.md',
]

REQUIRED_MERMAID = [
    'AGENTS.md',
    'templates/README.md',
    'docs/methodology/quickstart.md',
    'docs/methodology/anti-patterns.md',
    'docs/methodology/continuous-improvement-loop.md',
    'docs/methodology/definition-of-done.md',
    'docs/methodology/maturity-model.md',
    'docs/diagrams/README.md',
    'docs/loops/feature.md',
    'docs/loops/release.md',
    'docs/verifiers/README.md',
    'docs/evaluations/README.md',
    'docs/local-runner/README.md',
    'docs/adoption/README.md',
    'docs/operations/README.md',
    'docs/architecture/context-loading.md',
    'docs/architecture/context-engineering.md',
    'docs/prompts/quality.md',
    'docs/quality-system/README.md',
    'wiki/Home.md',
]

FORBIDDEN_TEXT = ['TODO', 'FIXME']
LINK_RE = re.compile(r'\[[^\]]+\]\(([^)]+)\)')
SKIP_PREFIXES = ('http://', 'https://', 'mailto:', '#')


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

forbidden_hits = []
for md in markdown:
    text = md.read_text(encoding='utf-8')
    for token in FORBIDDEN_TEXT:
        if token.lower() in text.lower():
            forbidden_hits.append(f'{md.relative_to(ROOT)} contains {token}')
fail('Forbidden work marker text found:', forbidden_hits)

broken_links = []
for md in markdown:
    text = md.read_text(encoding='utf-8')
    for match in LINK_RE.finditer(text):
        target = match.group(1).split('#', 1)[0].strip()
        if not target or target.startswith(SKIP_PREFIXES):
            continue
        resolved = (md.parent / target).resolve()
        try:
            resolved.relative_to(ROOT.resolve())
        except ValueError:
            continue
        if not resolved.exists():
            broken_links.append(f'{md.relative_to(ROOT)} -> {target}')
fail('Broken relative links:', broken_links)

print('Repository structure OK')
print('Required files checked:', len(REQUIRED))
print('Markdown files checked:', len(markdown))
