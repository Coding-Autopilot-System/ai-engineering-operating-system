import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class LinkTests(unittest.TestCase):
    def test_relative_links_are_valid(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / 'scripts' / 'check_links.py')],
            cwd=ROOT,
            text=True,
            capture_output=True,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


if __name__ == '__main__':
    unittest.main()
