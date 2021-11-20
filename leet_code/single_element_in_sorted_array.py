# https://leetcode.com/problems/single-element-in-a-sorted-array/
def find_single_element(nums):
    # (ques?) why the index didn't cross array limit
    start = 0
    end = len(nums) - 1
    while start < end:
        mid = (start + end) // 2
        # means odd index
        # [0,1,2,3]
        # [1,1,2,2]
        # first part of pair always should fall on even index
        if mid % 2:
            # (Notice) the number of if blocks could have been reduced if we did start =-1 in came of off mid
            if nums[mid] == nums[mid - 1]:
                start = mid + 1
            else:
                end = mid
        else:
            if nums[mid] == nums[mid + 1]:
                start = mid + 2
            else:
                end = mid
    # (ques?) how is the start pointing to the index we want
    return nums[start]


nums = [1, 1, 2, 3, 3, 4, 4, 8, 8]
print(find_single_element(nums))
