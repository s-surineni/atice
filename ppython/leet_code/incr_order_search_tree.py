def inorder(root):
    if not root:
        return
    yield inorder(root.left)
    yield root.val
    yield inorder(root.right)


def inc_ord_search_tree(root):
    res = TreeNode(None)

    for node in inorder(root):
        res.right = TreeNode(node)
        res = res.right
    return res.right
