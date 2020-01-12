class Solution(object):
    def sumEvenGrandparent(self, root):
        self.ans = 0
        def dfs(node, pval = -1, ppval = -1):
            if node:
                if ppval % 2 == 0:
                    self.ans += node.val
                dfs(node.left, node.val, pval)
                dfs(node.right, node.val, pval)

        dfs(root)
        return self.ans
