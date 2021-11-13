# https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/
def find_min_val(nums):
    min_val = 0
    summ = 0
    for val in nums:
        summ += val
        min_val = min(summ, min_val)
    return 1 - (min_val)


nums = [-3, 2, -3, 4, 2]
print(find_min_val(nums))
