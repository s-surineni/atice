class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def recoverFromPreorder(tree_str):
    stack, idx = [], 0
    while idx < len(tree_str):
        level, val = 0, ""
        while idx < len(tree_str) and tree_str[idx] == '-':
            level, idx = level + 1, idx + 1
        while idx < len(tree_str) and tree_str[idx] != '-':
            val, idx = val + tree_str[idx], idx + 1
        while len(stack) > level:
            stack.pop()
        node = TreeNode(val)
        if stack and stack[-1].left is None:
            stack[-1].left = node
        elif stack:
            stack[-1].right = node
        stack.append(node)
    return stack[0]


recoverFromPreorder("1-2--3--4-5--6--7")
