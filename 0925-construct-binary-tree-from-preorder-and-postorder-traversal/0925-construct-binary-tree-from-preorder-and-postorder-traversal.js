var constructFromPrePost = function (preorder, postorder) {
    return constructTree(0, preorder.length - 1, 0, preorder, postorder)
};

function constructTree(prestart, preend, poststart, preorder, postorder) {
    if (prestart > preend) return null;
    if (prestart === preend) return new TreeNode(preorder[prestart]);
    let left = preorder[prestart + 1];
    let numNodes = 1
    while (left != postorder[poststart + numNodes - 1]) {
        numNodes += 1
    }
    const root = new TreeNode(preorder[prestart])
    root.left = constructTree(prestart + 1, prestart + numNodes, poststart, preorder, postorder)
    root.right = constructTree(prestart + numNodes + 1,  preend, poststart + numNodes, preorder, postorder)
    return root;
}