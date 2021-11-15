# The official solution is different than what I did check how it would affects the performance !!

def find_end_points_and_steps(grid):
    steps = 0
    for ri in range(len(grid)):
        for ci in range(len(grid[ri])):
            if grid[ri][ci] == 0:
                steps += 1
            elif grid[ri][ci] == 1:
                sri, sci = ri, ci
            elif grid[ri][ci] == 2:
                eri, eci = ri, ci
    return steps, (sri, sci), (eri, eci)

def find_neighbors(grid, current_indices):
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

def find_unique_paths_dfs(grid, steps, current_indices, end_indices, unique_paths):
    # print('current_indices', current_indices)
    cr, cc = current_indices[0], current_indices[1]
    curr_val = grid[cr][cc]

    if curr_val  == 0:
        steps -= 1
        grid[cr][cc] = -1
    elif curr_val == 2 and steps == 0:
        unique_paths += 1
        return unique_paths
    elif curr_val == -1:
        return unique_paths
    elif curr_val == 1:
        grid[cr][cc] = -1
    else:
        return unique_paths
    for nr, nc in find_neighbors(grid, current_indices):
        unique_paths = find_unique_paths_dfs(grid, steps, (nr, nc), end_indices, unique_paths)

    grid[cr][cc] = 0
    return unique_paths

def find_unique_paths(grid):
    steps, start_indices, end_indices = find_end_points_and_steps(grid)

    unique_paths = find_unique_paths_dfs(grid, steps, start_indices, end_indices, 0)
    return unique_paths


def parse_input():
    grid = []

    while True:
        a_row = input('Enter rows separated by comma: ')
        if a_row == 'q':
            break
        a_row = [int(i) for i in a_row.split(',')]
        grid.append(a_row)

    return grid


grid = parse_input()
print(find_unique_paths(grid))
