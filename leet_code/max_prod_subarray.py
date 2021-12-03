def find_max_prod_subarray(nums):
    res, cmax, cmin = [nums[0]] * 3
    for idx, val in enumerate(nums[1:], start=1):
        if val < 0:
            cmax, cmin = cmin, cmax
        cmax = max(val * cmax, val)
        cmin = min(val * cmin, val)
        res = max(res, cmax)
    # print(cmin)
    return res


nums = [2, 3, -2, 4, 2]
print(find_max_prod_subarray(nums))
