# https://leetcode.com/problems/house-robber/
def find_max_profix(nums):
    incl = 0
    excl = 0
    for val in nums:
        temp = incl
        incl = excl + val
        excl = max(temp, excl)
    return max(incl, excl)


nums = [1, 2, 3, 1]
print(find_max_profix(nums))
