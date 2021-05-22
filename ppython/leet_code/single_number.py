def find_single_num(arr):
    res = 0
    for val in arr:
        res ^= val
    return res
