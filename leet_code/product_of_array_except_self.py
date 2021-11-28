def find_product_of_array_except_self(nums):
    nums_len = len(nums)
    res = [1] * nums_len
    for idx in range(1, nums_len):
        res[idx] = nums[idx - 1] * res[idx - 1]
    right = 1
    for idx in range(nums_len - 1, -1, -1):
        res[idx] = right * res[idx]
        right *= nums[idx]
    return res


nums = [1, 2, 3, 4]
print(find_product_of_array_except_self(nums))
