# https://leetcode.com/problems/plus-one/
def do_plus_one(digits):
    dig_len = len(digits) - 1
    while dig_len >= 0:
        if digits[dig_len] + 1 == 10:
            digits[dig_len] = 0
            dig_len -= 1
        else:
            digits[dig_len] += 1
            return digits
    digits = [0] * (len(digits) + 1)
    digits[0] = 1
    return digits


digits = [1, 2, 3]
digits = [8, 9]
digits = [8, 9, 9, 9, 9]
digits = [9, 9, 9, 9, 9]

print(do_plus_one(digits))
