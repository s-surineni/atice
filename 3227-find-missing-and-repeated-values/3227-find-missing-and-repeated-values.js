/**
 * @param {number[][]} grid
 * @return {number[]}
 */
var findMissingAndRepeatedValues = function(grid) {
    const numSet = new Set();
    const res = [];
    for (let i = 0; i < grid.length; i++) {
        for (let j = 0; j < grid[i].length; j++) {
            if (numSet.has(grid[i][j])) {
                res.push(grid[i][j]);
                
            } else {
                numSet.add(grid[i][j]);
            }
        }
    }
    for (let i = 1; i <= grid.length * grid.length; i++) {
        if (!numSet.has(i)) {
            res.push(i);
            break;
        }
    }
    return res;
};

let grid = [[1,3],[2,2]];
console.log(findMissingAndRepeatedValues(grid));