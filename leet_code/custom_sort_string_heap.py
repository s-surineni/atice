import heapq
import sys


def custom_sort_string_heap(str1, str2):
    str_order = {ch: idx for idx, ch in enumerate(str1)}
    sort_heap = []
    for ch in str2:
        heapq.heappush(sort_heap, (str_order.get(ch, sys.maxsize), ch))

    sorted_str2 = []

    while sort_heap:
        sorted_str2.append(heapq.heappop(sort_heap))

    # print('*' * 80)
    # print('iron man sorted_str2', sorted_str2)
    return ''.join([ch for idx, ch in sorted_str2])


S = "cba"
T = "abcd"
print(custom_sort_string_heap(S, T))
