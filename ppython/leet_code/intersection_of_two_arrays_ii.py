from collections import Counter


def find_intersection_of_2_arrays(arr1, arr2):
    arr1_counter = Counter(arr1)
    intersection_res = []
    for val in arr2:
        if arr1_counter.get(val):
            intersection_res.append(val)
            arr1_counter[val] -= 1
    return intersection_res


nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print(find_intersection_of_2_arrays(nums1, nums2))
