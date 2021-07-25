# https://leetcode.com/problems/partition-array-into-disjoint-intervals/solution/
def partition_array(num_list):
    list_len = len(num_list)
    max_left = [None] * list_len
    max_left[0] = num_list[0]

    for idx in range(1, list_len):
        max_ele = max(num_list[idx], max_left[idx - 1])
        max_left[idx] = max_ele
    min_right = [None] * list_len
    min_right[-1] = num_list[-1]
    for idx in range(list_len - 2, -1, -1):
        min_right[idx] = min(num_list[idx], min_right[idx + 1])

    for idx in range(1, list_len):
        if min_right[idx] >= max_left[idx - 1]:
            return idx


num_list = [1, 1, 1, 0, 6, 12]
print(partition_array(num_list))
