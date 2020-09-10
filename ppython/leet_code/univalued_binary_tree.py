def find_if_tree_is_univalued_recur(node, val):
    if not node:
        return True
    res = find_if_tree_is_univalued_recur(node.left, val)
    if not res:
        return res
    if node.val != val:
        return False
    res = find_if_tree_is_univalued_recur(node.right, val)
    return res


def find_if_tree_is_univalued(node):
    return find_if_tree_is_univalued_recur(node, node.val)
