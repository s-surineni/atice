def pancakeSort(A):
    res = []
    for x in range(len(A), 1, -1):
        i = A.index(x)
        res.extend([i + 1, x])
        A = A[:i:-1] + A[:i]
    return res


arr = [3, 2, 4, 1]
print(pancakeSort(arr))
