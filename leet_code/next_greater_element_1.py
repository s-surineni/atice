# https://leetcode.com/problems/next-greater-element-i/
import sys


def find_next_greater_element(nums1, nums2):
    great_element_dict = {}
    stack = []
    stack.append(sys.maxsize)
    for val in nums2:
        if val > stack[-1]:
            while val > stack[-1]:
                great_element_dict[stack.pop()] = val
            stack.append(val)
        else:
            stack.append(val)
    while len(stack) > 1:
        great_element_dict[stack.pop()] = -1
    res = []
    for val in nums1:
        res.append(great_element_dict[val])
    return res


nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
print(find_next_greater_element(nums1, nums2))
