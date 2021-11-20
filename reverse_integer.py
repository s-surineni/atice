# https://leetcode.com/problems/reverse-integer/
def reverse_integer(num):
    if not num:
        return num
    res = 0
    sign = num // abs(num)
    num = abs(num)
    while num:
        res = (res * 10) + (num % 10)
        num //= 10
    res = sign * res
    if -(2 ** 31) <= res <= (2 ** 31) - 1:
        return res
    else:
        return 0


print(reverse_integer(123))
print(reverse_integer(210))
print(reverse_integer(200))
print(reverse_integer(-123))
