# https://www.hackerrank.com/challenges/angry-children/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=greedy-algorithms
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxMin function below.
def maxMin(k, arr):
    arr.sort()
    # print('arr', arr)
    k -= 1
    end = k
    min_diff = sys.maxsize
    while end < len(arr):
        curr_diff = arr[end] - arr[end - k]
        # print('curr_diff', curr_diff)
        if curr_diff < min_diff:
            min_diff = curr_diff
        end += 1
    return min_diff


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    k = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = maxMin(k, arr)
    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
