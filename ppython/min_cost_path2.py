# https://practice.geeksforgeeks.org/problems/minimum-cost-path/0
import sys


tc = int(input().strip())


    
def shortest_path(grid2d, row_size, col_size):
    def is_inside_grid(x, y):
        if not( x < row_size or y < col_size):
            return False

    dist_matrix = []

    for a_row in range(row_size):
        dist_matrix.append([sys.maxsize] * col_size)
    print(dist_matrix)

    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    path_cells = [(0, 0, 0)]

    while path_cells:
        min_dist_ind = 0
        min_dist = sys.maxsize
        for trk3 in range(len(path_cells)):
            if min_dist > path_cells[trk3][2]:
                min_dist_ind = trk3

        closest_cell = path_cells.pop(trk3)

        for trk in range(4):
            x = closest_cell[0] + dr[trk]
            y = closest_cell[1] + dc[trk]

            if not is_inside_grid(x, y):
                continue

            if dist_matrix[x][y] > dist_matrix[closest_cell[0]][closest_cell[1]] + grid2d[x][y]:
                if dist_matrix[x][y] != sys.maxsize:
                    for trk2 in range(len(path_cells)):
                        if (path_cells[trk2][0], path_cells[trk2][1]) == (x, y):
                            path_cells[trk2][2] = dist_matrix[closest_cell[0]][closest_cell[1]] + grid2d[x][y]
                            break
                    dist_matrix[x][y] = dist_matrix[closest_cell[0]][closest_cell[1]] + grid2d[x][y]
    print('dist_matrix')
    print(dist_matrix)


for a_tc in range(tc):
    size = int(input().strip())
    grid = input().strip().split()
    grid = [int(i) for i in grid]

    grid2d = []

    for trk in range(size):
        grid2d.append(grid[(trk* size):((trk + 1) * size)])
    print(grid2d)

    shortest_path(grid2d, size, size)
