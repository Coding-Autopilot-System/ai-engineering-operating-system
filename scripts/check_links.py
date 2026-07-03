from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
LINK_RE = re.compile(r'\[[^\]]+\]\(([^)]+)\)')
SKIP_PREFIXES = ('http://', 'https://', 'mailto:', '#')

errors = []
for md in ROOT.rglob('*.md'):
    text = md.read_text(encoding='utf-8')
    for match in LINK_RE.finditer(text):
        target = match.group(1).split('#', 1)[0].strip()
        if not target or target.startswith(SKIP_PREFIXES):
            continue
        if target.startswith('../') or target.startswith('./'):
            resolved = (md.parent / target).resolve()
        else:
            resolved = (md.parent / target).resolve()
        try:
            resolved.relative_to(ROOT.resolve())
        except ValueError:
            continue
        if not resolved.exists():
            errors.append(f'{md.relative_to(ROOT)} -> {target}')

if errors:
    print('Broken relative links:')
    for error in errors:
        print('-', error)
    raise SystemExit(1)

print('Relative links OK')
