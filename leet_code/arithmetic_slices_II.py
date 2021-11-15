# https://leetcode.com/problems/arithmetic-slices-ii-subsequence/
def find_arithmetic_slices(nums):
    # (Notice) here instead of using 2d array 2d dict is used to save space
    # see and learn if all 2d array problems can be changed this way
    num_len = len(nums)
    ans = 0
    dp_cache = {}
    for idx in range(num_len):
        dp_cache[idx] = {}
        for idx2 in range(idx):
            diff = nums[idx] - nums[idx2]
            seq_idx2 = dp_cache[idx2].get(diff, 0)
            origin = dp_cache[idx].get(diff, 0)
            dp_cache[idx][diff] = origin + seq_idx2 + 1
            ans += seq_idx2
    return ans


# nums = [2, 4, 6, 8, 10]
nums = [7, 7, 7, 7, 7]
print(find_arithmetic_slices(nums))
