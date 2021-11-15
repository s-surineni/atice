# https://leetcode.com/problems/move-zeroes/
def move_zeroes(nums):
    slow, fast = -1, 0
    nums_len = len(nums)
    while fast < nums_len:
        if nums[fast]:
            slow += 1
            nums[slow], nums[fast] = nums[fast], nums[slow]
        fast += 1
    return nums


nums = [0, 1, 0, 3, 12]
nums = [1, 0]
nums = [1, 0, 1]
print(move_zeroes(nums))
