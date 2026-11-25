"""Worst Fix Ever entry: write one commit message to /output/entry.txt.

The message is a one-line commit subject for a fix that backfired:
the bug is gone because the whole feature that carried it is gone.
"""

from pathlib import Path

ENTRY = "fix: removed the bug by removing the feature that had it"

MAX_CHARS = 100


def main() -> None:
    if not 1 <= len(ENTRY) <= MAX_CHARS:
        raise ValueError("entry must be 1-100 characters")
    if ENTRY != ENTRY.strip() or "\n" in ENTRY:
        raise ValueError("entry must be a single line with no surrounding whitespace")
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(ENTRY, encoding="utf-8")
    target.chmod(0o644)
    print(ENTRY)


if __name__ == "__main__":
    main()
