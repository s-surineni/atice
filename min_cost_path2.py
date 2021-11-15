# https://practice.geeksforgeeks.org/problems/minimum-cost-path/0
import sys


tc = int(input().strip())


class PriorityQueue():
    def __init__(self, size):
        self.curr_size = 0
        self.array= [None] * size
        self.position = {}      # stores position of vertex in array

    def is_empty(self):
        return self.curr_size == 0

    def min_heapify(self, idx):
        l_c = self.left_c_idx(idx)
        r_c = self.right_c_idx(idx)

        if l_c < self.curr_size and self.array[l_c][0] < self.array[idx][0]:
            smallest = l_c
        else:
            smallest = idx
        if r_c < self.curr_size and self.array[r_c][0] < self.array[smallest][0]:
            smallest = r_c
        if smallest != idx:
            self.swap(idx, smallest)
            self.min_heapify(smallest)

    def swap(self, i, j):
        self.position[self.array[i][1]] = j
        self.position[self.array[j][1]] = i
        self.array[i], self.array[j] = self.array[j], self.array[i]

    def left_c_idx(self, idx):
        return (2 * idx) + 1

    def right_c_idx(self, idx):
        return (2 * idx) + 2

    def par_idx(self, idx):
        return idx // 2

    def decrease_key(self, d_v, new_dist):
        idx = self.position[d_v[1]]
        self.array[idx] = (new_dist, d_v[1])
        while idx > 0 and self.array[self.par_idx(idx)][0] > self.array[idx][0]:
            self.swap(idx, self.par_idx(idx))
            idx = self.par_idx(idx)

    def insert(self, d_v):
        self.position[d_v[1]] = self.curr_size
        print('*' * 80)
        print('curr_size', self.curr_size)
        print('array', self.array)
        self.array[self.curr_size] = (sys.maxsize, d_v[1])
        self.curr_size += 1
        # self.array.append((sys.maxsize, d_v[1]))
        self.decrease_key((sys.maxsize, d_v[1]), d_v[0])

    def extract_min(self):
        print('*' * 80)
        print('self.array', self.array)
        print('self.position', self.position)
        min_node = self.array[0][1]
        self.array[0] = self.array[self.curr_size - 1]
        self.curr_size -= 1
        self.min_heapify(0)
        print('min_node', min_node)
        del self.position[min_node]
        return min_node


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

    p_q = PriorityQueue(row_size * col_size)
    p_q.insert((0, 0, 0))
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
