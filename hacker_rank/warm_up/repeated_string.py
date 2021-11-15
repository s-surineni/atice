# https://www.hackerrank.com/challenges/repeated-string/problem?h_r=profile
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    str_len = len(s)

    a_in_str = 0
    for a_char in s:
        if a_char == 'a':
            a_in_str += 1
    no_of_reps = n // str_len
    no_of_a = no_of_reps * a_in_str
    rest_of_char = n % str_len
    rest_of_str = s[:rest_of_char]

    for a_char in rest_of_str:
        if a_char == 'a':
            no_of_a += 1
    return no_of_a

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)
    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
