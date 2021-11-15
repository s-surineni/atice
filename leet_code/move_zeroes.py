# https://leetcode.com/problems/move-zeroes/
def move_zeroes(nums):
    ze, nz = 0, 0
    nums_len = len(nums)
    while ze < nums_len and nz < nums_len:
        while ze < nums_len and nums[ze] != 0:
            ze += 1
        while nz < nums_len and nums[nz] == 0:
            nz += 1
        if ze < nums_len and nz < nums_len and ze < nz:
            nums[ze], nums[nz] = nums[nz], nums[ze]
        else:
            nz += 1
    return nums


nums = [0, 1, 0, 3, 12]
nums = [1, 0]
nums = [1, 0, 1]
print(move_zeroes(nums))
