# https://leetcode.com/problems/maximum-depth-of-binary-tree
def find_max_depth_recur(root, res, curr):
    if not root:
        return max(res, curr)
    curr += 1
    lres = find_max_depth_recur(root.left, res, curr)
    rres = find_max_depth_recur(root.right, res, curr)
    return max(lres, rres)


"""
(Better) simple and effective
public int maxDepth(TreeNode root) {
        if(root==null){
            return 0;
        }
        return 1+Math.max(maxDepth(root.left),maxDepth(root.right));
    }
"""


def find_max_depth(root):
    return find_max_depth_recur(root, 0, 0)
