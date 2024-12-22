"""
Username  : lcastillov
Problem   : Day 13: Claw Contraption (1)
Date      : 12/22/2024
Time      : O(10^4 x N)
Execution : python3 part-one-version-1.py < input.txt
"""

import sys
import re

DELTA_RE = r"^.*?: X[\+=](\d+), Y[\+=](\d+)"


def xy(s):
    return map(int, re.match(DELTA_RE, s).groups())


if __name__ == "__main__":
    conf = [line.strip() for line in sys.stdin.readlines() if len(line.strip()) > 0]

    sol = 0
    for i in range(0, len(conf), 3):
        xa, ya = xy(conf[i])
        xb, yb = xy(conf[i + 1])
        xp, yp = xy(conf[i + 2])
        best = -1
        for a in range(101):
            for b in range(101):
                x = xa * a + xb * b
                y = ya * a + yb * b
                if x == xp and y == yp and (best == -1 or 3 * a + b < best):
                    best = 3 * a + b
        if best != -1:
            sol += best

    print(sol)
