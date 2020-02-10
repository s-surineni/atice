from collections import defaultdict


def sort_matrix_diagonally(mat):
    diagonal_dict = defaultdict(list)
    for ri, row in enumerate(mat):
        for ci, val in enumerate(row):
            diagonal_dict[ri-ci].append(val)

    print(diagonal_dict)
    rows = len(mat)
    cols = len(mat[0])

    for k in diagonal_dict:
        diagonal_dict[k] = sorted(diagonal_dict[k])

    for ri in range(rows):
        for ci in range(cols):
            mat[ri][ci] = diagonal_dict[ri-ci].pop(0)

    return mat

mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
print(sort_matrix_diagonally(mat))
