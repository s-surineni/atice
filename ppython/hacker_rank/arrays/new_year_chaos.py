#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    q_len = len(q)
    total_count = 0
    for idx in range(q_len - 1, -1, -1):
        # curr_count = 0
        if idx + 1 != q[idx]:
            turn = 1
            while idx + 1 != q[idx]:
                q[idx], q[idx - turn] = q[idx - turn], q[idx]
                turn += 1
            # Could have tested this inside while loop and would have saved
            # some steps <!better>
            if turn > 3:
                print('Too chaotic')
                return
            total_count += (turn - 1)
    print(total_count)
if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
