# https://www.hackerrank.com/challenges/sock-merchant/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    color_count = {}
    pairs = 0
    for color in ar:
        if color in color_count:
            color_count[color] += 1
            if color_count[color] % 2 == 0:
                pairs += 1
        else:
            color_count[color] = 1
    return pairs


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

