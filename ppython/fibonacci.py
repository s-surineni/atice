# https://practice.geeksforgeeks.org/problems/fibonacci-to-n/0
test_cases = int(input().strip())

def print_fib(num1, num2, end_num):
    # print('n1n2en', num1, num2, end_num)
    if num2 <= end_num:
        print(num2, end=' ')

        temp = num2
        num2 = num1 + num2
        num1 = temp
        print_fib(num1, num2, end_num)
    
for a_tc in range(test_cases):
    end_num = int(input().strip())
    num1 = 0
    num2 = 1

    if num1 < end_num:
        print(num1, end=' ')
    print_fib(num1, num2, end_num)
    print()
