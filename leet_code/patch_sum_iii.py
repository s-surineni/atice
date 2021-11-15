# https://leetcode.com/problems/path-sum-iii/submissions/
def find_path_sum_recur(root, target, cache, run_sum):
    if not root:
        return 0
    # print(root.val, cache, run_sum)

    curr_sum = root.val + run_sum
    req_sum = curr_sum - target
    res = 0
    if req_sum in cache:
        res = cache[req_sum]
    if curr_sum == target:
        res += 1
    # (Notice) there was an issue when this statement is added before calculating res
    cache[curr_sum] = cache.get(curr_sum, 0) + 1

    # print('res', res)
    res += find_path_sum_recur(root.left, target, cache, curr_sum)
    res += find_path_sum_recur(root.right, target, cache, curr_sum)
    cache[curr_sum] -= 1
    return res


def find_path_sum(root, target):
    cache = {}
    return find_path_sum_recur(root, target, cache, 0)
