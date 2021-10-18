# https://leetcode.com/problems/cousins-in-binary-tree/
from collections import deque


def find_cousins(root, val1, val2):
    qu = deque()
    qu.append(root, 0)
    # (Better) level size could be calculated as level_size = len(qu)
    level_size = 1
    next_level = 0
    found1 = False
    found2 = False
    while qu:
        while level_size:
            node = qu.popleft()
            if val1 == node.val:
                found1 = True
            elif val2 == node.val:
                found2 = True
            l_c = node.left.val
            r_c = node.right.val
            if l_c == val1 and r_c == val2:
                return False
            elif l_c == val2 and r_c == val1:
                return False
            if l_c:
                qu.append(l_c)
                next_level += 1
            if r_c:
                qu.append(r_c)
                next_level += 1

            level_size -= 1
        if found1 and found2:
            return True
        if found1 or found2:
            return False
        level_size = next_level
        next_level = 0
    return False
