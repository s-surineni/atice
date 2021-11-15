def check_array_formation(arr, pieces):
    mpp = {ar[0]: ar for ar in pieces}
    idx = 0
    while idx < len(arr):
        arr2 = mpp.get(arr[idx])
        if not arr2:
            return False
        for val in arr2:
            if val != arr[idx]:
                return False
            idx += 1
    return True


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

arr = [85]
pieces = [[85]]
print(check_array_formation(arr, pieces))
