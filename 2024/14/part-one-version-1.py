"""
Username  : lcastillov
Problem   : Day 14: Restroom Redoubt (1)
Date      : 12/22/2024
Time      : O(N)
Execution : python3 part-one-version-1.py < input.txt
"""

import sys
import re

ROBOT_RE = r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)"

if __name__ == "__main__":
    robots = [line.strip() for line in sys.stdin.readlines()]

    # W, T, S = 11, 7, 100
    W, T, S = 101, 103, 100

    Q = [0, 0, 0, 0]
    for robot in robots:
        px, py, vx, vy = map(int, re.match(ROBOT_RE, robot).groups())
        x = (px + vx * S) % W
        y = (py + vy * S) % T
        if x != W // 2 and y != T // 2:
            Q[2 * int(x < W // 2) + int(y < T // 2)] += 1

    print(Q[0] * Q[1] * Q[2] * Q[3])
