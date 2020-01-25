# how can we assume that when we reach at a point with same number of steps left
# remaining grid would look exactly same?

from functools import lru_cache

grid = []

def parse_input():
    grid = []

    while True:
        a_row = input('Enter rows separated by comma: ')
        if a_row == 'q':
            break
        a_row = [int(i) for i in a_row.split(',')]
        grid.append(a_row)

    return grid

def find_neighbors(current_indices):
    cr, cc = current_indices[0], current_indices[1]
    neighbours = []
    if cr - 1 >= 0:
        neighbours.append((cr - 1 , cc))
    if cc + 1 < len(grid[0]):
        neighbours.append((cr, cc + 1))
    if cr + 1 < len(grid):
        neighbours.append((cr + 1, cc))
    if cc - 1 >= 0:
        neighbours.append((cr, cc - 1))
    return neighbours


def code(r, c, co):
    return 1 << (r * co + c)

@lru_cache
def find_unique_paths_dp(curr_ids, end_ids, travel, co, ups):
    cr, cc = curr_ids[0], curr_ids[1]
    er, ec = end_ids[0], end_ids[1]

    if (cr, cc) == (er, ec) and travel == 0:
        # print('ups', ups)
        return 1
    ups = 0                     # TODO: find why without this I am getting very large ans !?
    for nr, nc in find_neighbors((cr, cc), ):
        if travel & code(nr, nc, co):        
            ups += find_unique_paths_dp((nr, nc), end_ids, travel ^ code(nr, nc, co), co, ups)
    print('cr, cc', cr, cc)
    print('ups', ups)
    return ups
    

def find_unique_paths(grid):
    travel = 0

    for r, row in enumerate(grid):
        for c, val in enumerate(row):
            if val % 2 == 0:
                travel |= code(r, c, len(row))
                if val == 2:
                    tr, tc = r, c
            elif val == 1:
                sr, sc = r, c
    return find_unique_paths_dp((sr, sc), (tr, tc), travel, len(row), 0)

grid = parse_input()

print(find_unique_paths(grid))
