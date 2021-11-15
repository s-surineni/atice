# https://leetcode.com/problems/n-th-tribonacci-number/


def find_trib_num(nth):
    if nth == 0:
        return 0
    elif nth == 1:
        return 1
    elif nth == 2:
        return 1
    n1, n2, n3 = 0, 1, 1

    for idx in range(3, nth + 1):
        n1, n2, n3 = n2, n3, n3 + n2 + n1
    return n3


def find_trib_num_start(nth):
    cache = {}
    if nth not in cache:
        cache[nth] = find_trib_num(nth)
    return cache[nth]


print(find_trib_num_start(4))
print(find_trib_num_start(5))
print(find_trib_num_start(6))
