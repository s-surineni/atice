from collections import deque
import sys


token = '|'


def find_max_level_sum_of_binary_tree(root):
    lq = deque()
    lq.append(root)
    lq.append(token)
    max_ls = - sys.maxsize
    cur_ls = 0
    while lq:
        ce = lq.popleft()
        if ce == token:
            if cur_ls > max_ls:
                max_ls = cur_ls
            cur_ls = 0
            lq.append(token)
        cur_ls += ce.val
    return max_ls
