# https://leetcode.com/problems/perfect-squares
from collections import deque
import decs


@decs.calculate_time
def find_perfect_square_sum(num):
    qu = deque()

    qu.append((num, 0))

    while qu:
        curr_num, depth = qu.popleft()
        sq = 1
        while curr_num - (sq ** 2) >= 0:
            diff = curr_num - (sq ** 2)
            if diff == 0:
                return depth + 1
            qu.append((diff, depth + 1))
            sq += 1

print(find_perfect_square_sum(12))
print(find_perfect_square_sum(122))
print(find_perfect_square_sum(1222))
