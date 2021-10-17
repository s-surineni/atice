# https://leetcode.com/problems/perfect-squares
import sys
import decs


@decs.calculate_time
def find_perfect_square_sum(num):
    cache = {}
    cache[0] = 0
    cache[1] = 1
    for val in range(2, num + 1):
        min_val = sys.maxsize
        sq_rt = 1
        while (val - (sq_rt ** 2)) >= 0:
            min_val = min(min_val, cache[val - (sq_rt ** 2)] + 1)
            sq_rt += 1
        cache[val] = min_val
    return cache[num]


print(find_perfect_square_sum(12))
print(find_perfect_square_sum(122))
print(find_perfect_square_sum(1222))

