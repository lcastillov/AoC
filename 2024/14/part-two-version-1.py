"""
Username  : lcastillov
Problem   : Day 14: Restroom Redoubt (2)
Date      : 12/22/2024
Time      : ???
Execution : python3 part-two-version-1.py < input.txt
Notes     : I searched online, and people said they  just
            looked for robots arranged  in  a  horizontal
            line. It seems there's a way to calculate the
            entropy and search for that instead.
"""

import os
import re
import sys
import time

ROBOT_RE = r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)"

W = 101
T = 103


def read():
    lines = [line.strip() for line in sys.stdin.readlines()]
    robots, Q = [], [[0] * W for _ in range(T)]
    for robot in lines:
        px, py, vx, vy = map(int, re.match(ROBOT_RE, robot).groups())
        robots.append([px, py, vx, vy])
        Q[py][px] += 1
    return robots, Q


def draw(Q, start=time.time()):
    """
    Draw a single arrangement  of  the  robots
    on the map and display  how  many  seconds
    have passed since the  start.  This  helps
    track the time if we're drawing in a loop.
    """
    os.system("clear")
    print("=== ROBOTS IN MOTION (%s sec) ===" % int(time.time() - start))
    for i in range(T):
        print("".join(str(Q[i][j]) if Q[i][j] else " " for j in range(W)))
    time.sleep(1 / 64)


def move(robots, Q, delta=1):
    for i in range(len(robots)):
        px, py, vx, vy = robots[i]
        Q[py][px] -= 1
        px = (px + vx * delta) % W
        py = (py + vy * delta) % T
        Q[py][px] += 1
        robots[i][0] = px
        robots[i][1] = py


def find_max_horizontal_line(Q):
    longest = 0
    for i in range(T):
        current = 0
        for j in range(W):
            current = current + 1 if Q[i][j] > 0 else 0
            longest = max(longest, current)
    return longest


if __name__ == "__main__":
    robots, Q = read()

    # Find the first robot arrangement
    # where the longest line is at least
    # 10 cells.
    iteration = 0
    while find_max_horizontal_line(Q) < 10:
        move(robots, Q)
        iteration += 1

    # Save the number of iterations to
    # print later.
    solution = iteration

    # Move all robots to their original
    # positions.
    move(robots, Q, -solution)

    # Start simulating and drawing all bot
    # positions, but we will speed up  the
    # process by setting how many ~seconds
    # the animation should last.
    steps = iteration // (64 * 5)
    start = time.time()
    while iteration > 0:
        delta = steps if iteration >= steps else 1
        move(robots, Q, delta)
        draw(Q, start)
        iteration -= delta

    print("SOLUTION = %d" % solution)
