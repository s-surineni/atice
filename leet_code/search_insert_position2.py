# https://leetcode.com/problems/search-insert-position/
def search_insert_position_recur(nums, target, st, ed):
    # (Better) this is shorter than the one I wrote
    # TODO find the logic behind this
    if st > ed:
        return st
    mid = (st + ed) // 2
    if nums[mid] < target:
        return search_insert_position_recur(nums, target, mid + 1, ed)
    elif nums[mid] > target:
        return search_insert_position_recur(nums, target, st, mid - 1)
    else:
        return mid


def search_insert_position(nums, target):
    return search_insert_position_recur(nums, target, 0, len(nums) - 1)


nums = [1, 3, 5, 6]
target = 5
nums = [1, 3]
target = 0
nums = [1, 3]
target = 2
print(search_insert_position(nums, target))
