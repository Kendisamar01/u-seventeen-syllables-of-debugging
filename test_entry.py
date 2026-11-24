import re
import subprocess
import sys
import unittest
from pathlib import Path

OUTPUT = Path("/output/entry.txt")
MAIN = Path(__file__).with_name("main.py")
VOWELS = "aeiouy"


def syllable_count(word: str) -> int:
    word = word.lower()
    groups = re.findall(r"[aeiouy]+", word)
    count = len(groups)
    if (
        len(groups) > 1
        and word.endswith("e")
        and not word.endswith("le")
        and word[-2] not in VOWELS
    ):
        count -= 1
    return max(count, 1)


def line_syllables(line: str) -> int:
    words = re.findall(r"[a-z]+", line.lower())
    return sum(syllable_count(word) for word in words)


class EntryTest(unittest.TestCase):
    def test_entry(self):
        subprocess.run([sys.executable, str(MAIN)], check=True)
        text = OUTPUT.read_bytes().decode("utf-8")
        self.assertGreaterEqual(len(text), 1)
        self.assertLessEqual(len(text), 200)
        lines = text.splitlines()
        self.assertEqual(len(lines), 3)
        self.assertTrue(all(line.strip() for line in lines))

    def test_syllables(self):
        subprocess.run([sys.executable, str(MAIN)], check=True)
        lines = OUTPUT.read_text(encoding="utf-8").splitlines()
        counts = [line_syllables(line) for line in lines]
        self.assertEqual(counts, [5, 7, 5])
        self.assertEqual(sum(counts), 17)


if __name__ == "__main__":
    unittest.main()
