#!/usr/bin/env python3
"""Sorry, I Heard That Wrong -- make.fun entry.

Writes the smart speaker's apology to /output/entry.txt.
Pure Python standard library, no third-party packages.
"""

import os
from pathlib import Path

LINE = "Sorry \u2014 I heard 'play jazz' as 'blame jazz', so I have spent the last hour accusing the saxophone."


def main() -> None:
    # Gate self-check: UTF-8 text, 1 to 140 characters, a single non-blank line.
    if not 1 <= len(LINE) <= 140:
        raise SystemExit(f"entry is {len(LINE)} characters, gate allows 1-140")
    if "\n" in LINE or not LINE.strip():
        raise SystemExit("entry must be a single non-blank line")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(LINE + "\n", encoding="utf-8")
    print(LINE)


if __name__ == "__main__":
    main()
