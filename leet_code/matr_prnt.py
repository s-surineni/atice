# 3, 3


# [00, 02]
# [20, 22]
# [00, 01, 02]
# [10, 11, 12]
# [20, 21, 22]

# 2 x 2
def print_max_diagonally(mat):
    rows = len(mat)
    cols = len(mat[0])

    for diag in range(rows):    # 0, 1, 2
        ri, ji = diag, 0
        for ri in range(diag, -1, -1): # diag = 1   1, 0
            print(mat[ri][ji], end=' ')
            ji += 1
        print()


    for diag in range(rows - 1, 0, -1):    # 2, 1
        ri = rows - 1
        ji = ri -
        for ri in range(diag, -1, -1): # diag = 1   1, 0
            print(mat[ri][ji], end=' ')
            ji += 1
        print()



mat = [['a', 'b', 'c'],
       ['d', 'e', 'f'],
       ['g', 'h', 'i']]

print(print_max_diagonally(mat))
