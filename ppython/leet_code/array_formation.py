def check_array_formation(arr, pieces):
    idx = 0
    while idx < len(arr):
        # val = arr[idx]
        res = False
        for arr2 in pieces:
            if idx == len(arr):
                return res
            if arr[idx] == arr2[0]:
                for val2 in arr2:
                    if arr[idx] != val2:
                        return False
                    idx += 1
                res = True
        if not res:
            return res
    return res


arr = [49, 18, 16]
pieces = [[16, 18, 49]]

arr = [15, 88]
pieces = [[88], [15]]
arr = [2, 82, 79, 95, 28]
pieces = [[2], [82], [28], [79, 95]]

arr = [91, 4, 64, 78]
pieces = [[78], [4, 64], [91]]

arr = [49, 18, 16]
pieces = [[16, 18, 49]]
print(check_array_formation(arr, pieces))
