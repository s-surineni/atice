# https://leetcode.com/problems/contains-duplicate/
def check_duplicate(nums):
    cache = set()
    for val in nums:
        if val in cache:
            return True
        cache.add(val)
    return False


nums = [1, 2, 3, 1]
print(check_duplicate(nums))
