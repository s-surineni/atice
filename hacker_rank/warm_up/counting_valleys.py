# https://www.hackerrank.com/challenges/counting-valleys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    valleys = 0
    level = 0
    # in_valley = False
    for step in s:
        if step == 'U':
            level += 1
        else:
            level -= 1
        # if level < 0 and not in_valley:
            # in_valley = True
        if step == 'U' and level == 0:
            valleys += 1
            # in_valley = False
    return (valleys)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
