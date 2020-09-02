# https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/
def find_num_of_submat(matrix, target):
    rows, cols = len(matrix), len(matrix[0])
    for row in matrix:
        for idx in range(len(row) - 1):
            row[idx + 1] += row[idx]
    # print('*' * 80)
    # print('iron man matrix', matrix)
    res = 0
    for st_c in range(cols):
        for ed_c in range(st_c, cols):
            sumt = 0
            sum_dict = {}
            sum_dict[0] = 1
            for rw in range(rows):
                sumt += matrix[rw][ed_c] - (matrix[rw][st_c - 1] if st_c > 0 else 0)
                res += sum_dict.get(sumt - target, 0)
                sum_dict[sumt] = sum_dict.get(sumt, 0) + 1
    return res


matrix = [[0, 1, 0], [1, 1, 1], [0, 1, 0]]
print(find_num_of_submat(matrix, 0))
