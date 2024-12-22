"""
Username  : lcastillov
Problem   : Day 13: Claw Contraption (2)
Date      : 12/22/2024
Time      : O(N)
Execution : python3 part-two-version-1.py < input.txt
"""

import sys
import re

DELTA_RE = r"^.*?: X[\+=](\d+), Y[\+=](\d+)"


def xy(s):
    return map(int, re.match(DELTA_RE, s).groups())


def idiv(n, d):
    if d != 0 and n % abs(d) == 0:
        result = n // d
        if result >= 0:
            return result
    return None


if __name__ == "__main__":
    conf = [line.strip() for line in sys.stdin.readlines() if len(line.strip()) > 0]

    sol = 0
    for i in range(0, len(conf), 3):
        xa, ya = xy(conf[i])
        xb, yb = xy(conf[i + 1])
        xp, yp = xy(conf[i + 2])
        xp += 10000000000000
        yp += 10000000000000

        B = idiv(xa * yp - xp * ya, xa * yb - xb * ya)
        if B is not None:
            A = idiv(xp - xb * B, xa)
            if A is not None:
                sol += 3 * A + B

    print(sol)
