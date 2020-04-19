def inorder(root, new_node):
    if not root:
        return new_node
    new_node = inorder(root.left, new_node)
    new_node.right = root
    new_node.left = None
    new_node = new_node.right
    new_node = inorder(root.right, new_node)
    return new_node
