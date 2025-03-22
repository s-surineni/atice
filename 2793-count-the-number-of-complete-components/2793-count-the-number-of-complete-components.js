class UnionFind {
    constructor(size) {
        this.parent = new Array(size).fill(0).map((_, idx) => idx);
        this.rank = new Array(size).fill(1);
    }

    find(x) {
        if (this.parent[x] !== x) {
            this.parent[x] = this.find(this.parent[x]);
        }
        return this.parent[x];
    }

    union(x, y) {
        let rootX = this.find(x);
        let rootY = this.find(y);
        if (rootX !== rootY) {
            if (this.rank[rootX] > this.rank[rootY]) {
                this.parent[rootY] = rootX;
                this.rank[rootX] += this.rank[rootY];
            } else {
                this.parent[rootX] = rootY;
                this.rank[rootY] += this.rank[rootX];
            }
        }
    }
}

/**
 * @param {number} n
 * @param {number[][]} edges
 * @return {number}
 */
var countCompleteComponents = function(n, edges) {
    const uf = new UnionFind(n);
    for (const [u, v] of edges) {
        uf.union(u, v);
    }

    const edgeCount = {}
    for (const [u, v] of edges) {
        const parent = uf.find(u);
        edgeCount[parent] = (edgeCount[parent] || 0) + 1;
    }
    let completeCount = 0;
    for (let vert = 0; vert < n; vert++) {
        if (uf.find(vert) === vert) {
            const grpSize = uf.rank[vert];
            const expectedEdges = grpSize * (grpSize - 1) / 2;
            if ((edgeCount[vert] || 0) === expectedEdges) {
                completeCount++;
            }
        }
    }
    return completeCount;
};