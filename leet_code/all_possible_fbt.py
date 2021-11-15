class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def clone(self, tree: TreeNode) -> TreeNode:
        if not tree:
            return None
        new_tree = TreeNode(0)
        new_tree.left = self.clone(tree.left)
        new_tree.right = self.clone(tree.right)
        return new_tree

    def allPossibleFBT(self, N):
        if N % 2 == 0:
            return []
        elif N == 1:
            return [TreeNode(0)]
        ret = []
        for part_nodes in range(1, N, 2):
            left_branch = self.allPossibleFBT(part_nodes)
            right_branch = self.allPossibleFBT(N - part_nodes - 1)
            for left_count, left in enumerate(left_branch, 1):
                for right_count, right in enumerate(right_branch, 1):
                    tree = TreeNode(0)
                    
                    # If we're using the last right branch, then this will be the last time this left branch is used and can hence
                    # be shallow copied, otherwise the tree will have to be cloned
                    tree.left = self.clone(left) if right_count < len(right_branch) else left
                    
                    # If we're using the last left branch, then this will be the last time this right branch is used and can hence
                    # be shallow copied, otherwise the tree will have to be cloned
                    tree.right = self.clone(right) if left_count < len(left_branch) else right
                    
                    ret.append(tree)
        return ret


print(Solution().allPossibleFBT(5))
