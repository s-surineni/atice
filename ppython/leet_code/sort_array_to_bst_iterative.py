class Tree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def sort_arr_to_bst(nums):
    stck = []
    mid = (0 + len(nums) - 1) // 2
    root = Tree(None)
    stck.append([root, 0, len(nums) - 1])

    while stck:
        curr_node, st, ed = stck.pop()
        if st <= ed:
            mid = (st + ed) // 2
            curr_node.val = nums[mid]
            curr_node.left = Tree(None)
            stck.append((curr_node.left, st, mid - 1))
            curr_node.right = Tree(None)
            stck.append((curr_node.right, mid + 1, ed))
    return root


print(sort_arr_to_bst([-10,-3,0,5,9]))
