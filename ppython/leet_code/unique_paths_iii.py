# https://leetcode.com/problems/unique-paths-iii/
def dfs(grid, current, zeros, res):
    cx, cy = current
    if grid[cx][cy] == 2:
        if zeros == -1:
            return res + 1
        else:
            return res
    elif grid[cx][cy] == -1:
        return res
    grid[cx][cy] = -1
    for nx, ny in ((cx + 1, cy), (cx - 1, cy), (cx, cy + 1), (cx, cy - 1)):
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
            res = dfs(grid, (nx, ny), zeros - 1, res)
    grid[cx][cy] = 0
    return res


def find_unique_paths(grid):
    zeros = 0

    for rid, row in enumerate(grid):
        for cid, val in enumerate(row):
            if val == 0:
                zeros += 1
            elif val == 1:
                start = rid, cid

    return dfs(grid, start, zeros, 0)


grid = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]
print(find_unique_paths(grid))
