# https://leetcode.com/problems/sqrtx/
a_num = int(input('Please enter a number: ').strip())

low = 0
high = a_num

while low <= high:
    mid = (low + high) // 2

    if mid ** 2 <= a_num < (mid + 1) ** 2:
        break
    elif a_num < mid ** 2:
        high = mid
    else:
        low = mid + 1
    print(low, high)
print('sqrt of {} is {}'.format(a_num, mid))
