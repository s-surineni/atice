# https://leetcode.com/problems/palindrome-number/

def is_palindrome(num):
    num = str(num)
    return num == num[::-1]
