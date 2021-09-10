# https://leetcode.com/problems/largest-plus-sign/
def find_largest_plus_sign(size, mines):
    mines = {tuple(mine) for mine in mines}
    ans = 0
    dps = [[0] * size for _ in range(size)]

    for row in range(size):
        count = 0
        for col in range(size):
            if (row, col) in mines:
                dps[row][col] = 0
                count = 0
            else:
                dps[row][col] = count + 1
                count += 1
        count = 0
        for col in range(size - 1, -1, -1):
            count = 0 if (row, col) in mines else count + 1
            if count < dps[row][col]:
                dps[row][col] = count

    for col in range(size):
        count = 0
        for row in range(size):
            count = 0 if (row, col) in mines else count + 1
            if count < dps[row][col]:
                dps[row][col] = count
        count = 0
        for row in range(size - 1, -1, -1):
            count = 0 if (row, col) in mines else count + 1
            if count < dps[row][col]:
                dps[row][col] = count
            if dps[row][col] > ans:
                ans = dps[row][col]
            # if count < dps[row][col]:
            #     dps[row][col] = count
    return ans


n = 5
mines = [[4, 2]]
print(find_largest_plus_sign(n, mines))
