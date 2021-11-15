def minDeletionSize(self, A):
    return sum(list(col) != sorted(col) for col in zip(*A))


def del_col_to_make_sorted(mat):
    r_len = len(mat)
    c_len = len(mat[0])

    delete_cols = set()

    for cidx in range(c_len):
        for ridx in range(r_len - 1):
            if ord(mat[ridx][cidx]) > ord(mat[ridx + 1][cidx]):
                delete_cols.add(cidx)

    return len(delete_cols)


print(del_col_to_make_sorted(["cba","daf","ghi"]))
