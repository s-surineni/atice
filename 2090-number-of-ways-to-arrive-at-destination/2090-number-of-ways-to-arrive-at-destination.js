/**
 * @param {number} n
 * @param {number[][]} roads
 * @return {number}
 */
var countPaths = function(n, roads) {
    // define variable to store MOD = 1e9 + 7
    const MOD = 1e9 + 7;
    // create adjacency list to store the graph
    const graph = Array.from({ length: n }, () => []);
    // loop over the roads array and add the edges to the graph
    for (let [u, v, w] of roads) {
        graph[u].push([v, w]);
        graph[v].push([u, w]);
    }
    const minHeap = new MinPriorityQueue(node_weight => node_weight[1]);
    minHeap.enqueue([0, 0]);
    const shortestTime = new Array(n).fill(Infinity);
    const pathCount = new Array(n).fill(0);
    shortestTime[0] = 0;
    pathCount[0] = 1;
    while (minHeap.size() > 0) {
        const [node, time] = minHeap.dequeue();
        if (time > shortestTime[node]) {
            continue;
        }
        for (let [nextNode, nextTime] of graph[node]) {
            if (time + nextTime < shortestTime[nextNode]) {
                shortestTime[nextNode] = time + nextTime;
                pathCount[nextNode] = pathCount[node];
                minHeap.enqueue([nextNode, shortestTime[nextNode]]);
            } else if (time + nextTime === shortestTime[nextNode]) {
                pathCount[nextNode] = (pathCount[nextNode] + pathCount[node]) % MOD;
            }
        }
    }
    return pathCount[n - 1];
};