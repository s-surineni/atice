# https://www.hackerrank.com/challenges/2d-array/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    # print(arr)
    r_len = len(arr)
    c_len = len(arr[0])
    x, y = 0, 0
    max_hr_val = -(sys.maxint) - 1
    while x + 2 < r_len:
        while y + 2 < c_len:
            # print('x y', x, y)
            hr_sum = (arr[x][y] + arr [x][y + 1] + arr[x][y + 2] +
                      arr[x + 1][y + 1] +
                      arr[x + 2][y] + arr [x + 2][y + 1] + arr[x + 2][y + 2])
            if hr_sum > max_hr_val:
                max_hr_val = hr_sum
            # print('max_hr_val', max_hr_val)
            y += 1
        x += 1
        y = 0
    return max_hr_val

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)
    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
