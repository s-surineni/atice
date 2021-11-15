#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    arr.sort()
    # print(arr)
    min_abs = (sys.maxsize)
    for idx in range(len(arr) - 1):
        # print(arr[idx], arr[idx + 1])
        curr_diff = abs(arr[idx] - arr[idx + 1])
        # print(curr_diff)
        if min_abs > curr_diff:
            min_abs = curr_diff
    return min_abs


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)
    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
