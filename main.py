"""Write the poem about stopping to /output/entry.txt."""

import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "entry.txt"
DST = Path("/output/entry.txt")


def main() -> None:
    text = SRC.read_text(encoding="utf-8")
    if not text.strip() or not 1 <= len(text) <= 280:
        raise SystemExit("entry.txt must be 1-280 non-blank code points")
    DST.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SRC, DST)


if __name__ == "__main__":
    main()
