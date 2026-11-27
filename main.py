"""Write the funniest sick-day excuse, in one line, to /output/entry.txt.

The excuse is a bereavement claim for a goldfish, justified by an HR
loophole: the policy doesn't specify species. One line, no setup it does
not need.
Deterministic: the same single line on every run.
"""

import os
from pathlib import Path

EXCUSE = "My goldfish died and I need to grieve; HR's bereavement policy doesn't specify species."


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(EXCUSE, encoding="utf-8")


if __name__ == "__main__":
    main()
