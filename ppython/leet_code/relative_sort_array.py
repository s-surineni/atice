from collections import Counter


def relative_sort_array(arr1, arr2):
    arr1_counter = Counter(arr1)
    sorted_arr1 = []
    for val in arr2:
        sorted_arr1 += arr1_counter.pop(val) * [val]
    rem = list(arr1_counter.keys())
    rem.sort()
    for val in rem:
        sorted_arr1 += arr1_counter.pop(val) * [val]
    return sorted_arr1


arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
arr2 = [2, 1, 4, 3, 9, 6]
print(relative_sort_array(arr1, arr2))
