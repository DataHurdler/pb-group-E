"""Check that every module's timed outline adds up, and the day totals 360.

Usage: python3 tools/check_timing.py

For each modules/NN-*/README.md it reads the header line
    Time: HH:MM–HH:MM (NN min) · Talk T / do D
and the timed-outline rows whose first cell is "a–b". It checks that
  - the rows run contiguously from 0 to NN,
  - Talk + do equals NN,
  - the clock times span NN minutes, and
  - the modules together total 360 instructional minutes.
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EXPECTED_TOTAL = 360
HEADER = re.compile(
    r"^Time: (\d{1,2}):(\d{2})–(\d{1,2}):(\d{2}) \((\d+) min\) · Talk (\d+) / do (\d+)",
    re.M,
)
ROW = re.compile(r"^\| (\d+)–(\d+) \|", re.M)


def minutes(h, m):
    h, m = int(h), int(m)
    if h < 8:  # afternoon times written as 1:00, 2:05, ...
        h += 12
    return h * 60 + m


def check(path):
    text = path.read_text()
    problems = []
    header = HEADER.search(text)
    if not header:
        return 0, [f"{path.parent.name}: no 'Time: … · Talk T / do D' header"]
    h1, m1, h2, m2, length, talk, do = header.groups()
    length, talk, do = int(length), int(talk), int(do)
    if minutes(h2, m2) - minutes(h1, m1) != length:
        problems.append(f"clock span is {minutes(h2, m2) - minutes(h1, m1)}, header says {length}")
    if talk + do != length:
        problems.append(f"talk {talk} + do {do} = {talk + do}, not {length}")
    rows = [(int(a), int(b)) for a, b in ROW.findall(text)]
    if not rows:
        problems.append("no timed-outline rows")
    else:
        expected = 0
        for a, b in rows:
            if a != expected:
                problems.append(f"row {a}–{b} should start at {expected}")
            expected = b
        if expected != length:
            problems.append(f"outline ends at {expected}, not {length}")
    return length, [f"{path.parent.name}: {p}" for p in problems]


def main():
    total, problems = 0, []
    for readme in sorted((ROOT / "modules").glob("[0-9][0-9]-*/README.md")):
        length, issues = check(readme)
        total += length
        problems += issues
        print(f"{readme.parent.name:32} {length:4} min {'OK' if not issues else 'PROBLEM'}")
    print(f"{'total':32} {total:4} min")
    if total != EXPECTED_TOTAL:
        problems.append(f"day totals {total}, expected {EXPECTED_TOTAL}")
    for p in problems:
        print("  -", p)
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
