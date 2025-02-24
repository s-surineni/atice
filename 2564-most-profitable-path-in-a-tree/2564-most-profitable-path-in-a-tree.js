function calculateBobValues(currNode, bobPath, bob, adjList, visited) {
    if (currNode === bob) {
        bobPath[currNode] = 0;
        return 1;
    }
    visited[currNode] = true; // mark the current node as visited
    for (const neighbor of adjList[currNode]) {
        if (visited[neighbor]) continue; // skip visited nodes
        let res = calculateBobValues(neighbor, bobPath, bob, adjList, visited)
        if (res > 0) {
            bobPath[currNode] = res;
            return res + 1;
        }
    }
    return false;
}
function calculateAmount(bobTime, time, amount) {
    // check the time of bob with this node
    let res;
    if (bobTime < time) {
        // return 0; // bob has already visited this node
        res = 0; // bob has already visited this node
    } else if (bobTime === time) {
        res = amount / 2; // bob is at this node at the same time as alice
        // return amount / 2; // bob is at this node at the same time as alice
    } else { // bob has not visited this node yet
        res = amount; // bob has not visited this node yet
        // return amount;
    }
    return res;
}
function calculateMaxProfit(currNode, time, bobPath, amount, adjList, visited) {
    visited[currNode] = true; // mark the current node as visited
    // Base case: if currNode is a leaf node, return the amount of the node
    if (adjList[currNode].length === 0) {
        return calculateAmount(bobPath[currNode], time, amount[currNode]);
    }
    // Recursive case: calculate the maximum profit for each child node
    let maxProfit = -Infinity;
    let currAmount = calculateAmount(bobPath[currNode], time, amount[currNode]);
    for (const neighbor of adjList[currNode]) {
        if (visited[neighbor]) continue; // skip visited nodes
        let childProfit = calculateMaxProfit(neighbor, time + 1, bobPath, amount, adjList, visited);
        maxProfit = Math.max(maxProfit, childProfit);
    }
    return currAmount + (maxProfit === -Infinity ? 0 :  maxProfit);
}
var mostProfitablePath = function (edges, bob, amount) {
    const numNodes = edges.length + 1;
    // create array of size numNodes to store the adjacency list
    const adjList = new Array(numNodes).fill().map(() => []);
    // initialize adjList with edges
    for (const [u, v] of edges) {
        adjList[u].push(v);
        adjList[v].push(u);
    }
    // calculate node values after bob traversing
    const bobPath = new Array(numNodes).fill(Infinity);
    const visited = new Array(numNodes).fill(false);
    calculateBobValues(0, bobPath, bob, adjList, visited)
    console.log('ironman bobPath', JSON.stringify(bobPath));
    visited.fill(false);
    return calculateMaxProfit(0, 0, bobPath, amount, adjList, visited);
};