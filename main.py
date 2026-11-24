from pathlib import Path

HAIKU = (
    "Cursor blinks at three\n"
    "the log line swears it is clean\n"
    "I left that line in"
)


def main():
    path = Path("/output/entry.txt")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(HAIKU, encoding="utf-8")


if __name__ == "__main__":
    main()
