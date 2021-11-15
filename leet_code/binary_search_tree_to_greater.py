def BST_to_GST_rev_inorder(node, accumulated):
    if not node:
        return accumulated

    accumulated = BST_to_GST_rev_inorder(node.right, accumulated)
    accumulated += node.val
    node.val = accumulated
    accumulated = BST_to_GST_rev_inorder(node.left, accumulated)
    return accumulated

def BST_to_GST(root):
    return BST_to_GST_rev_inorder(root)
