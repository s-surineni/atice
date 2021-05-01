# https://leetcode.com/problems/sign-of-the-product-of-an-array/
def find_product_sign(nums):
    neg = 0
    for val in nums:
        if val < 0:
            neg += 1
        elif val == 0:
            return 0
    return -1 if neg %2 else 1
