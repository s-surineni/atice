/**
 * @param {number} n
 * @param {number[][]} edges
 * @param {number[][]} query
 * @return {number[]}
 */
class UnionFind {
    constructor(size) {
        this.parent = [];
        this.rank = [];
        for (let i = 0; i < size; i++) {
            this.parent[i] = i;
            this.rank[i] = 1;
        }
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
            } else if (this.rank[rootX] < this.rank[rootY]) {
                this.parent[rootX] = rootY;
            } else {
                this.parent[rootY] = rootX;
                this.rank[rootX] += 1;
            }
            return true;
        } else {
            return false;
        }
    }
}
var minimumCost = function(n, edges, query) {
    const unionFind = new UnionFind(n);
    const minPathCost = new Array(n).fill(-1);
    for (const edge of edges) {
        const root1 = unionFind.find(edge[1])
        const root2 = unionFind.find(edge[0])
        let root;
        if (root1 !== root2) {
            unionFind.union(edge[0], edge[1]);
            root = unionFind.find(edge[0]);
            minPathCost[root] &= minPathCost[root1] & minPathCost[root2];
            minPathCost[root] &= edge[2];

        } else {
            minPathCost[root1] &= edge[2];
        }
    }
    const answer = [];
    for (const q of query) {
        if (unionFind.find(q[0]) === unionFind.find(q[1])) {
            answer.push(minPathCost[unionFind.find(q[0])]);
        } else {
            answer.push(-1);
        }
    }
    return answer;
};

