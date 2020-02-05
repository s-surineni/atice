def number_of_submatrices_that_sum_to_target(mat, target):
    if not mat or len(mat) == 0 or len(mat[0]) == 0:
        return 0

    rows = len(mat)
    cols = len(mat[0])

    prefix_sum_arr = [[] for _ in range(rows + 1)]

    prefix_sum_arr[0] = [0] * cols

    for idx, curr_row in enumerate(mat):
        for idy, val in enumerate(curr_row):
            prefix_sum_arr[idx + 1].append(prefix_sum_arr[idx][idy] + mat[idx][idy])

    print('*' * 80)
    print('iron man prefix_sum_arr', prefix_sum_arr)
mat = [[0,1,0],[1,1,1],[0,1,0]]
target = 0
print(number_of_submatrices_that_sum_to_target(mat, target))
