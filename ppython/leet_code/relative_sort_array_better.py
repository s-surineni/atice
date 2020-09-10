# we'll
def relative_sort_array(arr1, arr2):
    bucket_count = [0] * 1000
    for num in arr1:
        bucket_count[num] += 1
    idx = 0
    for num in arr2:
        while bucket_count[num]:
            arr1[idx] = num
            idx += 1
            bucket_count[num] -= 1
    for idx2, val in enumerate(bucket_count):
        while val:
            arr1[idx] = idx2
            idx += 1
            val -= 1
    return arr1


arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
arr2 = [2, 1, 4, 3, 9, 6]
print(relative_sort_array(arr1, arr2))
