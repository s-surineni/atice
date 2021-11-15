# https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/
a_num = int(input().strip())

curr_num = a_num
num_sum = 0
num_prod = 1


while curr_num > 0:
    curr_digit = curr_num % 10
    num_prod *= curr_digit
    num_sum += curr_digit
    curr_num //= 10

# print(num_prod)
# print(num_sum)

res = num_prod - num_sum

print(res)
