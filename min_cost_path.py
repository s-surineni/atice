# https://www.geeksforgeeks.org/dynamic-programming-set-6-min-cost-path/

cost_matrix = [[1, 2, 3],
               [4, 8, 2],
               [1, 5, 3]]


def find_min_cost_matrix(cost_matrix):
    row_size = len(cost_matrix)
    col_size = len(cost_matrix[0])

    min_cost_matrix = [[0 for x in range(col_size)] for x in range(row_size)]

    min_cost_matrix[0][0] = cost_matrix[0][0]
    for col in range(1, row_size):
        min_cost_matrix[0][col] = (min_cost_matrix[0][col - 1] +
                                   cost_matrix[0][col])

    for row in range(1, col_size):
        min_cost_matrix[row][0] = (min_cost_matrix[row - 1][0] +
                                   cost_matrix[row][0])

    for row in range(1, col_size):
        for col in range(1, row_size):
            min_cost_matrix[row][col] = (min(
                min_cost_matrix[row - 1][col],
                min_cost_matrix[row][col - 1],
                min_cost_matrix[row - 1][col - 1]) +
                                         cost_matrix[row][col])
    print(min_cost_matrix)

find_min_cost_matrix(cost_matrix)
