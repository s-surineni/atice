def find_depth_of_node(root, ans):
    if not root: return 0, 0

    lans, ans = find_depth_of_node(root.left, ans)
    rans, ans = find_depth_of_node(root.right, ans)
    diameter = lans + rans + 1
    ans = max(ans, diameter)
    return diameter, ans

def find_diameter_of_tree(root):
    max_depth, ans = find_depth_of_node(root, 0)
