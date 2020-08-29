# https://leetcode.com/problems/subarray-sum-equals-k/discuss/341399/Python-clear-explanation-with-code-and-example
def find_sub_array_sum(nums, val):
    res = 0
    cu_sum = 0
    cu_sum_dict = {}
    cu_sum_dict[0] = 1

    for el in nums:
        cu_sum += el
        res += cu_sum_dict.get(cu_sum - val, 0)
        cu_sum_dict[cu_sum] = cu_sum_dict.get(cu_sum, 0) + 1
    return res
