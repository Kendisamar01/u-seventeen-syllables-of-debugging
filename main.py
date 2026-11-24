from pathlib import Path

LINES = (
    "Cursor blinks at three",
    "one log line swears it is clean",
    "I left that line in",
)

ENTRY = "\n".join(LINES)
OUTPUT = Path("/output/entry.txt")


def write_entry(path: Path = OUTPUT) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(ENTRY + "\n", encoding="utf-8")


if __name__ == "__main__":
    write_entry()
