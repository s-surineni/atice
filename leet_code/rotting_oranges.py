# https://leetcode.com/problems/rotting-oranges/
from collections import deque


def find_rotting_oranges(grid):
    qu = deque()
    rlen = len(grid)
    clen = len(grid[0])
    fresh_count = 0
    for ridx, row in enumerate(grid):
        for cidx, val in enumerate(row):
            if val == 1:
                fresh_count += 1
            elif val == 2:
                qu.append((ridx, cidx))
    time = 0
    while qu and fresh_count > 0:
        wall_size = len(qu)
        time += 1
        for _ in range(wall_size):
            rid, cid = qu.popleft()
            for x, y in (
                (rid - 1, cid),
                (rid, cid - 1),
                (rid + 1, cid),
                (rid, cid + 1),
            ):
                if 0 <= x < rlen and 0 <= y < clen:
                    if grid[x][y] == 1:
                        fresh_count -= 1
                        grid[x][y] = 2
                        qu.append((x, y))

    if fresh_count:
        return -1
    else:
        return time


grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
print(find_rotting_oranges(grid))
