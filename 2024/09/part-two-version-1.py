"""
Username  : lcastillov
Problem   : Day 9: Disk Fragmenter (2)
Date      : 12/21/2024
Time      : O(N^2)
Execution : python part-two-version-1.py < input.txt
"""

import sys


if __name__ == "__main__":
    ins = sys.stdin.readline().strip()

    files = []
    offset = 0
    for i, c in enumerate(ins):
        if i % 2 == 0:
            files.append((len(files), offset, int(c)))
        offset += int(c)

    for id in range(len(files) - 1, -1, -1):
        idx = next(i for i, (fid, _, _) in enumerate(files) if fid == id)

        k = 0
        while k < idx and (
            files[k + 1][1] - (files[k][1] + files[k][2]) < files[idx][2]
        ):
            k += 1

        if k < idx:
            _, offset, size = files.pop(idx)
            files.insert(k + 1, (id, files[k][1] + files[k][2], size))

    ans = 0
    for fid, offset, size in files:
        ans += fid * size * (offset + offset + size - 1) // 2

    print(ans)
