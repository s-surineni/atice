# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
def find_min_in_rotated(nums):
    lo, hi = 0, len(nums) - 1
    if len(nums) == 1:
        return nums[0]
    if nums[hi] > nums[lo]:
        return nums[lo]

    while lo <= hi:
        # (Notice) in leetcode they found mid as mid = left + (right - left) / 2
        mid = (lo + hi) // 2
        if nums[mid - 1] > nums[mid]:
            return nums[mid]
        elif nums[mid + 1] < nums[mid]:
            return nums[mid + 1]
        elif nums[0] < nums[mid]:
            lo = mid + 1
        else:
            hi = mid - 1


# nums = [3, 4, 5, 1, 2]
nums = [4, 5, 6, 7, 0, 1, 2]

print(find_min_in_rotated(nums))
