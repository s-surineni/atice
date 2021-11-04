# https://leetcode.com/problems/sum-root-to-leaf-numbers/
def sum_root_leaf_recur(node, num, res):
    if not node:
        return res
    if node:
        print("node val", node.val)
        num = (num * 10) + node.val
        print("num", num)
    if not (node.left or node.right):
        res += num
        return res
    res = sum_root_leaf_recur(node.left, num, res)
    res = sum_root_leaf_recur(node.right, num, res)
    return res


def sum_root_leaf(root):
    return sum_root_leaf_recur(root, 0, 0)
