def delete_node(root, key):
    if not (root):
        return
    if root.val > key:
        root.left = delete_node(root.left, key)
    elif root.val < key:
        root.right = delete_node(root.right, key)
    else:
        if not root.right:
            return root.left
        if not root.left:
            return root.right
        curr_node = root.right
        while curr_node.left:
            curr_node = curr_node.left
        root.val = curr_node.val
        # because the least value in right subtree could have
        # right subtree itself,
        # we need to call delete on the least value in right subtree so that it child replaces it
        # as we already know it will be in the right subtree we call only on right subtree
        root.right = delete_node(root.right, curr_node.val)
    return root
