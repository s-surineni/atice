#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    mag_hash = {}
    for word in magazine:
        if word in mag_hash:
            mag_hash[word] += 1
        else:
            mag_hash[word] = 1
    for word in note:
        if word in magazine and mag_hash[word]:
            mag_hash[word] -= 1
        else:
            print('No')
            break
    else:
        print('Yes')
if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
