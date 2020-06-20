def get_matrix_count(matrix, rid, cid):
    rlen = len(matrix)
    clen = len(matrix[0])

    if 0 < rid < rlen and 0 < cid < clen:
        neighbors = [0] * 3
        # min(matrix[r-1][c-1], matrix[r][c-1], matrix[r-1][c]) + matrix[r][c]
        # <!better> this would avoid needing an extra list
        for idx, (x, y) in enumerate([(rid, cid - 1), (rid - 1, cid - 1),
                                      (rid - 1, cid)]):
            neighbors[idx] = matrix[x][y]
        cell_val = min(neighbors) + 1
        matrix[rid][cid] = cell_val
        return cell_val
    else:
        return 1


def count_square_submatrices(matrix):
    tot_square_rect = 0
    for rid, row in enumerate(matrix):
        for cid, ele in enumerate(row):
            if ele:
                tot_square_rect += get_matrix_count(matrix, rid, cid)
    return tot_square_rect


if __name__ == '__main__':
    matrix = [[0, 1, 1, 1], [1, 1, 1, 1], [0, 1, 1, 1]]
    print(count_square_submatrices(matrix))
