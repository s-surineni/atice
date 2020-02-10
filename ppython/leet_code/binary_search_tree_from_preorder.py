import bisect


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def bst_from_pre(pre_mat, idx, bound):
    if idx >= len(pre_mat) or pre_mat[idx] > bound:
        return None, idx

    root = TreeNode(pre_mat[idx])
    idx += 1
    root.left, idx = bst_from_pre(pre_mat, idx, root.val)
    root.right, idx = bst_from_pre(pre_mat, idx, bound)
    return root, idx


mat = [8,5,1,7,10,12]

bst_from_pre(mat, 0, float('inf'))

