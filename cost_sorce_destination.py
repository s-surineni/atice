def find_least_cost_recur(curr, end, grid, cache):
    x, y = curr
    print('*' * 80)
    print('iron man curr, end', curr, end)
    if curr == end:
        return grid[end[0]][end[1]]
    if cache[x][y] != -1:
        return cache[x][y]
    # right x, y + 1
    # down x + 1, y
    resr = []
    for xd, yd in ((0, 1), (1, 0)):
        if x + xd <= end[0] and y + yd <= end[1]:
            resr.append(
                find_least_cost_recur((x + xd, y + yd), end, grid, cache))
    cache[x][y] = min(resr) + grid[x][y]
    return cache[x][y]


# [[3, 4],
# [2, 5]]
# [[-1,  -1,],
# [-1, -1]]
def find_lest_cost():
    start = (0, 0)

    # grid = [[3, 4, 5, 1, 2], [3, 6, 2, 3, 4], [3, 2, 4, 5, 6], [2, 3, 1, 2, 3]]
    # grid = [[3, 4],
    #         [2, 5]]
    # grid = [[3, 1],
    #         [2, 5]]
    # grid = [[1, 8, 9],
    #         [1, 1, 5]]
    grid = [[1, 8, 9],
            [1, 100, 5]]
    rlen = len(grid)
    clen = len(grid[0])
    end = (rlen - 1, clen - 1)
    cache = [[-1] * clen for _ in range(rlen)]
    return find_least_cost_recur(start, end, grid, cache)


print(find_lest_cost())
