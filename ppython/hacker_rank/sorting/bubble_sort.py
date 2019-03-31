# https://www.hackerrank.com/challenges/ctci-bubble-sort/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):
    swaps = 0
    for it in range(len(a)):
        for idx in range(len(a) - it - 1):
            if a[idx] > a[idx + 1]:
                a[idx], a[idx + 1] = a[idx + 1], a[idx]
                swaps += 1
    print('Array is sorted in {} swaps.'.format(swaps))
    print('First Element: {}'.format(a[0]))
    print('Last Element: {}'.format(a[-1]))


if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
