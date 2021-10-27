# https://leetcode.com/problems/invert-binary-tree/
def rev_bin_tree(root):
    if not root:
        return
    # print("root", root.val)
    left = rev_bin_tree(root.right)
    # if left:
    # print("left", left.val)
    right = rev_bin_tree(root.left)
    # if right:
    # print("left", right.val)
    root.left = left
    root.right = right
    return root
