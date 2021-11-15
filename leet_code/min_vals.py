#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'segment' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER x
#  2. INTEGER_ARRAY space
#
import sys

def segment(x, space):
    space_len = len(space)
    if space_len == 1:
        return space[0]
    idx = 0

    tot_min = - 1
    curr_min = -1
    while idx + x < space_len:
        # curr_min = min(space[idx: idx + x])
        # if tot_min < curr_min:
        #     tot_min = curr_min
        # idx += 1
        if curr_min < 0:
            curr_min = min(space[idx: idx + x])
        elif space[idx + x] < curr_min:
            curr_min = space[idx + x]
        print('curr_min', curr_min)

        if curr_min > tot_min:
            tot_min = curr_min
        if space[idx] == curr_min:
            curr_min = -1
        idx += 1

    return tot_min
