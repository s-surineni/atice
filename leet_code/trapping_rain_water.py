# Trapping Rain Water
def find_trapped_water(builds):
    list_len = len(builds)
    left_max = [0] * list_len
    left_max[0] = builds[0]

    for idx in range(1, list_len):
        left_max[idx] = max(left_max[idx - 1], builds[idx])

    right_max = [0] * list_len
    right_max[-1] = builds[-1]

    for idx in range(list_len - 2, -1, -1):
        right_max[idx] = max(right_max[idx + 1], builds[idx])

    res = 0
    for idx in range(1, list_len - 1):
        res += min(left_max[idx], right_max[idx]) - builds[idx]
    return res


builds = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(find_trapped_water(builds))
