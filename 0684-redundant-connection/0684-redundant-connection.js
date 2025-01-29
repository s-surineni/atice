var findRedundantConnection = function(edges) {
    const nodeLen = edges.length;
    const root = new Array(nodeLen).fill(0).map((_, i) => i);

    function findParent(node) {
        if (root[node] !== node) {
            root[node] = findParent(root[node]);
        }
        return root[node];
    }

    function union(node1, node2) {
        const parent1 = findParent(node1);
        const parent2 = findParent(node2);
        if (parent1 !== parent2) {
            root[parent2] = parent1;
        }
    }

    function isConnected(node1, node2) {
        return findParent(node1) === findParent(node2);
    }

    for(const [node1, node2] of edges) {
        if (isConnected(node1, node2)) {
            return [node1, node2];
        }
        union(node1, node2);
    }
    return [];

};