def inorder_rec(root, curr_depth, max_depth):
    curr_depth += 1

    if not root.children:
        return max(curr_depth, max_depth)


    for ch in root.children:
        max_depth = inorder_rec(ch, curr_depth, max_depth)

    return max_depth

