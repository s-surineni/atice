#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    z_arr = [0] * n
    max_el = 0
    for op in queries:
        for idx in range(op[0] - 1, op[1]):
            z_arr[idx] += op[2]
            if max_el < z_arr[idx]:
                max_el = z_arr[idx]
    # print(z_arr)
    print(max_el)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    # fptr.write(str(result) + '\n')

    # fptr.close()
