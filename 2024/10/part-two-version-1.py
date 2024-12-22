"""
Username  : lcastillov
Problem   : Day 10: Hoof It (2)
Date      : 12/21/2024
Time      : O(N^2) -- very low constant
Execution : python3 part-two-version-1.py < input.txt
"""

import sys


if __name__ == "__main__":
    topo = [list(map(int, line.strip())) for line in sys.stdin.readlines()]

    R, C = len(topo), len(topo[0])
    visited = [[0] * C for _ in range(R)]

    def trailheads(i, j):
        if topo[i][j] == 9:
            return 1

        ans = 0
        for di, dj in ((-1, 0), (+1, 0), (0, +1), (0, -1)):
            ii, jj = i + di, j + dj
            if 0 <= ii < R and 0 <= jj < C and topo[ii][jj] - topo[i][j] == 1:
                ans += trailheads(ii, jj)

        return ans

    solution = 0
    for i in range(R):
        for j in range(C):
            if topo[i][j] == 0:
                solution += trailheads(i, j)

    print(solution)
