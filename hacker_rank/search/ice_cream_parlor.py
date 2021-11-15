#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the whatFlavors function below.
def whatFlavors(cost, money):
    # print('cost money', cost, money)
    
    for c in cost:
        if money - c in cost:
            if c == money - c:
                if cost.count(c) != 2:
                    continue
            print(cost.index(c) + 1, cost.index(money - c, cost.index(c) + 1) + 1)
            break

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        money = int(input())

        n = int(input())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)
