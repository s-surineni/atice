def find_maximum_contiguous_subarray(nums):
    max_sum = nums[0]
    curr_sum = nums[0]
    idx = 1
    # (Better) could have appended negative number at end to avoid special case
    while idx < len(nums):

        if curr_sum < 0:
            curr_sum = 0
        curr_sum += nums[idx]
        if curr_sum > max_sum:
            max_sum = curr_sum
        idx += 1
    return max_sum


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
nums = [5, 4, -1, 7, 8]
print(find_maximum_contiguous_subarray(nums))
