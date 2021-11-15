def find_island_perimeter(grid):
    peri = 0
    rcount = len(grid)
    cols = len(grid[0])
    for rid, row in enumerate(grid):
        for cid, val in enumerate(row):
            if not val:
                continue
            if not cid or not grid[rid][cid - 1]:
                peri += 1
            if cid == cols - 1 or not grid[rid][cid + 1]:
                peri += 1
            if not rid or not grid[rid - 1][cid]:
                peri += 1
            if rid == rcount - 1 or not grid[rid + 1][cid]:
                peri += 1
    return peri


grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
# grid = [[1]]
# grid = [[1, 0]]
print(find_island_perimeter(grid))
