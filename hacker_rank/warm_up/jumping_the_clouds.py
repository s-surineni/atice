#!/bin/python3
# https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    idx = 0
    jump = 0
    # -1 because we need not jump once we reach the end
    while idx < (len(c) - 1):
        if (idx + 2) < len(c) and c[idx + 2] == 0:
            idx += 2
        else:
            idx += 1
        jump += 1
    return jump

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
