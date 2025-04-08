var minimumOperations = function(nums) {
    const numIdx = {};
    let minOps = 0;
    for (let idx = 0; idx < nums.length; idx++) {
        const currNum = nums[idx];
        if (numIdx[currNum] === undefined) {
            numIdx[currNum] = idx;
        } else {
            minOps = Math.max(minOps, Math.ceil((numIdx[currNum] + 1) / 3))
            numIdx[currNum] = idx;
        }
    }
    return minOps;
};