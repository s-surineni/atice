# https://leetcode.com/problems/single-number-iii/
def find_single_number(nums):
    a_xor_b = 0
    for val in nums:
        a_xor_b ^= val
    right_most = a_xor_b & -a_xor_b

    right_set_nums = []
    for val in nums:
        if val & right_most:
            right_set_nums.append(val)

    num1 = 0
    for val in right_set_nums:
        num1 ^= val

    num2 = num1 ^ a_xor_b
    return [num1, num2]


nums = [1, 2, 1, 3, 2, 5]
print(find_single_number(nums))
