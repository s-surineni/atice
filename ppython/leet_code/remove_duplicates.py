# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
def remove_duplicates(nums):
    cid = 0
    ddid = 1
    while ddid < len(nums):
        if nums[ddid] == nums[ddid - 1]:
            ddid += 1
        else:
            cid += 1
            nums[cid] = nums[ddid]
            ddid += 1
    return cid


# nums = [1, 1, 2]
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(remove_duplicates(nums))
print(nums)
