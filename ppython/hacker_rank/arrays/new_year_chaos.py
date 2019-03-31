#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    bribes = 0
    for idx in range(len(q) - 1):
        if q[idx] > q[idx + 1]:
            if q[idx] - q[idx + 1] > 2:
                print('Too chaotic')
                break
            bribes += q[idx] - (idx)
    else:
        print(bribes)

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
