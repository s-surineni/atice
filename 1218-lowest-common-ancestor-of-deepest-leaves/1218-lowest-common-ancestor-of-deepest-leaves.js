/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {TreeNode}
 */
function findLCA(node) {
    if (!node) return [null, 0];
    const [leftNode, leftDepth] = findLCA(node.left);
    const [rightNode, rightDepth] = findLCA(node.right);
    if (leftDepth === rightDepth) {
        return [node, leftDepth + 1];
    }
    if (leftDepth > rightDepth) {
        return [leftNode, leftDepth + 1];
    }
    if (rightDepth > leftDepth) {
        return [rightNode, rightDepth + 1];
    }
}
var lcaDeepestLeaves = function(root) {

    return findLCA(root)[0];
};