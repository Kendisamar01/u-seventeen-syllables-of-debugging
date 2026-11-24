import subprocess
import sys
import unittest
from pathlib import Path

OUTPUT = Path("/output/entry.txt")
MAIN = Path(__file__).with_name("main.py")


class EntryTest(unittest.TestCase):
    def test_entry(self):
        subprocess.run([sys.executable, str(MAIN)], check=True)
        text = OUTPUT.read_bytes().decode("utf-8")
        self.assertGreaterEqual(len(text), 1)
        self.assertLessEqual(len(text), 200)
        lines = text.splitlines()
        self.assertEqual(len(lines), 3)
        self.assertTrue(all(line.strip() for line in lines))


if __name__ == "__main__":
    unittest.main()
