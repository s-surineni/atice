# https://practice.geeksforgeeks.org/problems/minimum-cost-path/0
import sys


tc = int(input().strip())


    
def shortest_path(grid2d, row_size, col_size):
    def is_inside_grid(x, y):
        if (x >= row_size or y >= col_size or x < 0 or y < 0):
            return False
        else:
            return True

    dist_matrix = []

    for a_row in range(row_size):
        dist_matrix.append([sys.maxsize] * col_size)
    dist_matrix[0][0] = grid2d[0][0]
    # print(dist_matrix)

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
        # print('*' * 80)
        # print('closest_cell', closest_cell)


        for trk in range(4):
            x = closest_cell[0] + dr[trk]
            y = closest_cell[1] + dc[trk]

            if not is_inside_grid(x, y):
                continue
            # print('after continue')
            # print('x , y ', x, y)
            # print('sum', dist_matrix[closest_cell[0]][closest_cell[1]] + grid2d[x][y])
            if dist_matrix[x][y] > dist_matrix[closest_cell[0]][closest_cell[1]] + grid2d[x][y]:
                # print('inside distance comparison')
                if dist_matrix[x][y] != sys.maxsize:
                    for trk2 in range(len(path_cells)):
                        if (path_cells[trk2][0], path_cells[trk2][1]) == (x, y):
                            path_cells[trk2][2] = dist_matrix[closest_cell[0]][closest_cell[1]] + grid2d[x][y]
                            break
                    else:
                        path_cells.append([x, y, dist_matrix[x][y]])
                else:
                    path_cells.append([x, y, dist_matrix[x][y]])

                dist_matrix[x][y] = dist_matrix[closest_cell[0]][closest_cell[1]] + grid2d[x][y]
    # print('dist_matrix')
    # print(dist_matrix)
    print(dist_matrix[row_size - 1][col_size - 1])

for a_tc in range(tc):
    size = int(input().strip())
    grid = input().strip().split()
    grid = [int(i) for i in grid]

    grid2d = []

    for trk in range(size):
        grid2d.append(grid[(trk* size):((trk + 1) * size)])
    # print(grid2d)

    shortest_path(grid2d, size, size)
