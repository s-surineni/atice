import heapq
import sys


def find_smallest_range(num_lists):
    list_ct = len(num_lists)
    next_arr = [0] * list_ct
    num_heap = []
    max_val = 0
    min_range = None
    diff = sys.maxsize
    for idx, idx2 in enumerate(next_arr):
        heapq.heappush(num_heap, (num_lists[idx][idx2], idx, idx2))
        max_val = max(max_val, num_lists[idx][idx2])

    while True:
        min_val, list_num, min_idx = heapq.heappop(num_heap)
        # min_val = num_lists[list_num][min_idx]
        cdiff = max_val - min_val
        if cdiff < diff:
            diff = cdiff
            min_range = [min_val, max_val]
        min_idx += 1
        if min_idx == len(num_lists[list_num]):
            return min_range
        next_val = num_lists[list_num][min_idx]
        if next_val > max_val:
            max_val = next_val
        heapq.heappush(num_heap, (next_val, list_num, min_idx))
    # print(num_heap)
    # print('iron man max_val', max_val)


# nums = [[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]
nums = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
print(find_smallest_range(nums))
