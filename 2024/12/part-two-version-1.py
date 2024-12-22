"""
Username  : lcastillov
Problem   : Day 12: Garden Groups (2)
Date      : 12/22/2024
Time      : O(NM)
Execution : python3 part-two-version-1.py < input.txt
"""

import sys

if __name__ == "__main__":
    garden = [line.strip() for line in sys.stdin.readlines()]

    R, C = len(garden), len(garden[0])
    Q, S = [], [[False] * C for _ in range(R)]

    def at(r, c):
        if 0 <= r < R and 0 <= c < C:
            return garden[r][c]
        return None

    solution = 0
    for i in range(R):
        for j in range(C):
            if S[i][j]:
                continue

            Q.append((i, j))
            S[i][j] = True
            sides, area = 0, 0

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
                        # We'll ensure the current cell (r, c) is the first cell contributing
                        # to the side it belongs to, in the direction (dr, dc). To do this, we
                        # need to check that the previous cell is not the first contributor. Here,
                        # "first" and "previous" refer to the direction we're considering. For
                        # example, a cell (r, c) with direction (-1, 0) is the first contributor
                        # to the north-facing side if the cell at (r, c+1) is not contributing
                        # north. The tricky part is properly shuffling the dr's and dc's around.
                        if not (
                            garden[r][c] == at(r - dc, c - dr)
                            and garden[r][c] != at(r - dc + dr, c - dr + dc)
                        ):
                            sides += 1
                    elif not S[nr][nc]:
                        Q.append((nr, nc))
                        S[nr][nc] = True

            solution += area * sides

    print(solution)
