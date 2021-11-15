# https://leetcode.com/problems/two-sum/
def find_two_sum(nums, tar):
    maps = {}
    for idx, val in enumerate(nums):
        diff = tar - val
        if diff in maps:
            return [maps[diff], idx]
        else:
            maps[val] = idx


nums = [2, 7, 11, 15]
target = 9
print(find_two_sum(nums, target))
