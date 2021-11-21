# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
def construct_bin_tree_from_in_post_recur(in_values, inorder, postorder, start, end):
    # print('post',postorder)
    # print('start, end', start, end)
    if start > end:
        return None
    root_val = postorder.pop()
    root = TreeNode(root_val)
    mid = in_values[root_val]
    root.right = construct_bin_tree_from_in_post_recur(
        in_values, inorder, postorder, mid + 1, end
    )
    root.left = construct_bin_tree_from_in_post_recur(
        in_values, inorder, postorder, start, mid - 1
    )
    return root


def construct_bin_tree_from_in_post(inorder, postorder):
    in_values = {val: idx for idx, val in enumerate(inorder)}
    return construct_bin_tree_from_in_post_recur(
        in_values, inorder, postorder, 0, len(inorder) - 1
    )
