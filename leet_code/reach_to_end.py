# linked list
# each node has link to the next node and random pointer
# random function
# least number of random calls steps to reach end
# a -> b -> c -> d -> e -> f
# 1 ->
# fun -> 8
# fun -> 6

# 1 -> 2 -> 3 -> 4 -> 5 -> 6

import sys

cache = [0] * 6
def calc_min_steps(curr, last, steps, cache, res):
    # if cache[curr]:
    #     return cache[curr]
    if cache[curr]:
        if steps > cache[curr]:
            return sys.maxsize
    if curr.random == last:
        cache[curr] = steps + 1
    elif curr.val + 5 <= last:
        cache[curr] = steps + 1
    curr_steps = sys.maxsize
    for step in range(1, 6):
        curr_steps = min(curr_steps, calc_min_steps(curr + step, last, step + 1, cache))
    cache[curr] = curr_steps
