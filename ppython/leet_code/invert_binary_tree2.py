# https://leetcode.com/problems/invert-binary-tree/
def invert_binary_tree(root):
    oroot = root
    stck = []
    stck.append(root)

    while stck:
        root = stck.pop()
        if not root:
            continue
        # print(root.val)
        root.left, root.right = root.right, root.left
        stck.append(root.left)
        stck.append(root.right)
    return oroot
