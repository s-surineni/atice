def find_leaf_nodes(root, leaf_list):
    if not root:
        return True
    left_val = find_leaf_nodes(root.left, leaf_list)
    right_val = find_leaf_nodes(root.right, leaf_list)
    if left_val and right_val:
        leaf_list.append(root.val)
    return False


def find_if_leaf_similar(root1, root2):
    list1 = []
    list2 = []
    find_leaf_nodes(root1, list1)
    find_leaf_nodes(root2, list2)
    return list1 == list2
