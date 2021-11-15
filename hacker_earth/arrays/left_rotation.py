#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    print(a)
    print(d)
    arr_len = len(a)
    new_arr = [0] * arr_len
    for idx in range(arr_len):
        new_arr[idx] = a[(idx + d) % arr_len]
    return new_arr

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    # fptr.write(' '.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
