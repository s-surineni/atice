
var FindElements = function(root) {
    this.root = root;
    this.root.val = 0;
    this.values = new Set();
    this.values.add(0);
    const recover = (node) => {  // Changed to arrow function to preserve 'this' context
        if (node === null) return;
        if (node.left !== null) {
            node.left.val = 2 * node.val + 1;
            this.values.add(node.left.val);
            recover(node.left);
        }
        if (node.right !== null) {
            node.right.val = 2 * node.val + 2;
            this.values.add(node.right.val);
            recover(node.right);
        }
    }
    recover(this.root);
};

/** 
 * @param {number} target
 * @return {boolean}
 */
FindElements.prototype.find = function(target) {
    // Check if the target value exists in the set of recovered values
    return this.values.has(target);
};
/** 
 * Your FindElements object will be instantiated and called as such:
 * var obj = new FindElements(root)
 * var param_1 = obj.find(target)
 */