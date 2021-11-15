def find_score_after_flipping_matrix(matrix):
    ros, cos = len(matrix), len(matrix[0])
    res = ros * (1 << cos - 1)

    for a_c in range(1, cos):
        cur = sum(matrix[ri][a_c] == matrix[ri][0] for ri in range(ros))
        res += max(cur, ros - cur) * (1 << cos - 1 - a_c)
    return res


if __name__ == '__main__':
    matrix = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
    print(find_score_after_flipping_matrix(matrix))
