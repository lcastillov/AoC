"""
Username  : lcastillov
Problem   : Day 12: Garden Groups (1)
Date      : 12/22/2024
Time      : O(NM)
Execution : python3 part-one-version-1.py < input.txt
"""

import sys

if __name__ == "__main__":
    garden = [line.strip() for line in sys.stdin.readlines()]

    R, C = len(garden), len(garden[0])
    Q, S = [], [[False] * C for _ in range(R)]

    solution = 0
    for i in range(R):
        for j in range(C):
            if S[i][j]:
                continue

            Q.append((i, j))
            S[i][j] = True
            perimeter, area = 0, 0

            while Q:
                area += 1
                (r, c) = Q.pop()
                for dr, dc in ((-1, 0), (+1, 0), (0, -1), (0, +1)):
                    nr, nc = r + dr, c + dc
                    if (
                        nr < 0
                        or nr >= R
                        or nc < 0
                        or nc >= C
                        or garden[r][c] != garden[nr][nc]
                    ):
                        perimeter += 1
                    elif not S[nr][nc]:
                        Q.append((nr, nc))
                        S[nr][nc] = True

            solution += area * perimeter

    print(solution)
