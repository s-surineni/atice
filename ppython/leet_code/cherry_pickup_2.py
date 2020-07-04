import sys


def find_max_cherry_picks_recur(field, dp_cache, cr, cc1, cc2):
    rows = len(field)
    cols = len(field[0])
    if cr == rows or cc1 == -1 or cc2 == -1 or cc2 == cols or cc1 == cols:
        return -sys.maxsize
    if dp_cache[cr][cc1][cc2]:
        return dp_cache[cr][cc1][cc2]
    max_pos = 0
    curr_pos_val = field[cr][cc1] + (0 if cc1 == cc2 else field[cr][cc2])
    for cc1r in [cc1 - 1, cc1, cc1 + 1]:
        for cc2r in [cc2 - 1, cc2, cc2 + 1]:
            max_pos = max(
                max_pos, find_max_cherry_picks_recur(field, dp_cache,
                                                     cr + 1, cc1r,
                                                     cc2r))
    dp_cache[cr][cc1][cc2] = max_pos + curr_pos_val
    return max_pos + curr_pos_val


def find_max_cherry_picks(field):
    rows = len(field)
    cols = len(field[0])
    dp_cache = []
    for ri in range(rows):
        curr_c1 = []
        for ci1 in range(cols):
            curr_c2 = [0] * cols
            curr_c1.append(curr_c2)
        dp_cache.append(curr_c1)
    return find_max_cherry_picks_recur(field, dp_cache, 0, 0, cols - 1)


if __name__ == '__main__':
    grid = [[3, 1, 1], [2, 5, 1], [1, 5, 5], [2, 1, 1]]
    print(find_max_cherry_picks(grid))
