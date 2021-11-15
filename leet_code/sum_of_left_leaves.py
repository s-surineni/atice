# https://leetcode.com/problems/sum-of-left-leaves/
def find_sum_of_left_leaves(root):
    # 3 - left 2 - right
    stack = [(root, 2)]
    res = 0
    while stack:
        node, dire = stack.pop()
        if not node:
            continue
        if not (node.left or node.right):
            if dire % 2:
                res += node.val
        stack.append((node.left, 3))
        stack.append((node.right, 2))
    return res
