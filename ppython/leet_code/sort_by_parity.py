def sort_by_parity(mat):
    op = 0
    ep = len(mat) - 1
    mat_len = len(mat)

    while True:
        while op < mat_len and not mat[op] % 2:
            op += 1
        while ep > -1 and mat[ep] % 2:
            ep -= 1
        if op < mat_len and ep > -1 and op < ep:
            mat[op], mat[ep] = mat[ep], mat[op]
            op, ep = op + 1, ep - 1
        else:
            break

    return mat


# mat = [3,1,2,4]
# mat = [0,2]
mat = [0,1]
print(sort_by_parity(mat))
