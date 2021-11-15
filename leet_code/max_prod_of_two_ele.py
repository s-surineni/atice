import sys


def max_product(nums):
    max1 = - sys.maxsize
    max2 = max1

    for val in nums:
        if val > max1:
            max2 = max1
            max1 = val
        elif val > max2:
            max2 = val

    return (max1 - 1) * (max2 - 1)
