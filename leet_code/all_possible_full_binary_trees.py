# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None


class Solution:
    def allPossibleFBT(self, N):
        if not N % 2:
            return 0
        if N == 1:
            return [TreeNode(0)]
        if N == 3:
            root = TreeNode(0)
            root.left = TreeNode(0)
            root.right = TreeNode(0)
            return [root]
        root = TreeNode(0)
        child_count = N - 1
        all_trees = []
        for le in range(1, child_count, 2):
            # print('ler', list(range(1, child_count, 2)))
            
            # left_count = allPossibleFBT(le)
            left_trees = self.allPossibleFBT(le)
            # print('lt', len(left_trees))
            # right_count = allPossibleFBT(child_count - le)
            right_trees = self.allPossibleFBT(child_count - le)
            # print('rt', len(right_trees))
            for a_lt in left_trees:
                for a_rt in right_trees:
                    root = TreeNode(0)
                    root.left = a_lt
                    root.right = a_rt
                    all_trees.append(root)
            # print(N, len(all_trees))
        return all_trees


# print(len(Solution().allPossibleFBT(5)))
