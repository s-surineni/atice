import sys
infi = sys.maxsize


def optimum_jump_backtrack(arr, curr_pos, cost, path_cost, path, res):
    if curr_pos in path or cost > res or curr_pos < 0:
        return infi
    if curr_pos > len(arr) - 1:
        if cost < res:
            res = cost
        return cost

    forward_cost = optimum_jump_backtrack(arr, curr_pos + 2,
                                          cost + arr[curr_pos], path_cost,
                                          path | {curr_pos}, res)
    backward_cost = optimum_jump_backtrack(arr, curr_pos - 1,
                                           cost + arr[curr_pos], path_cost,
                                           path | {curr_pos}, res)
    res = min(forward_cost, backward_cost)
    actual_cost = res - cost
    if path_cost[curr_pos] < actual_cost:
        path_cost[curr_pos] = actual_cost

    return res



nums = [1, 2, 3, 4, 100]
# nums = [1, 2, 3]
# nums = [1]
# nums = [1, 2]


def optimum_jump(nums):
    path_cost = [infi] * len(nums)
    return optimum_jump_backtrack(nums, 0, 0, path_cost, set(), infi)


print(optimum_jump(nums))
