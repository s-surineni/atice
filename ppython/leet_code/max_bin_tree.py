class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def max_bin_tree(nums):
    if not nums:
        return None
    max_idx, max_val = nums.index(max(nums)), max(nums)
    node = TreeNode(max_val)
    node.right = max_bin_tree(nums[max_idx + 1:])
    node.left = max_bin_tree(nums[:max_idx])
    return node
