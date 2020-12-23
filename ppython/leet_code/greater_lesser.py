# 3 4 5 6 7
# -1
def find_order(nums):
    if len(nums) == 1 or len(nums) == 0:
        return True
    order = None
    if nums[0] > nums[1]:
        order = 'decr'
    else:
        order = 'incr'

    idx = 1
    while idx < len(nums) - 1:
        if nums[idx] > nums[idx + 1] and order == 'incr':
            return False
        if nums[idx] < nums[idx + 1] and order == 'decr':
            return False
        idx += 1
    return True


vals = [3, 5, 6, 8]
vals = [9, 2, 1, 6]
print(find_order(vals))
