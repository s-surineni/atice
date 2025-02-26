var maxAbsoluteSum = function(nums) {
    let maxPre = -Infinity, minPre = Infinity, maxAbs = 0, pre = 0;

    for (let num of nums) {
        pre += num;
        maxPre = Math.max(maxPre, pre);
        minPre = Math.min(minPre, pre);
        if (pre >= 0) {
            maxAbs = Math.max(maxAbs, pre, pre - minPre);
        } else if (pre <= 0) {
            maxAbs = Math.max(maxAbs, Math.abs(pre), Math.abs(pre - maxPre));
        }
    }
    return maxAbs;
};

// Example usage:
console.log(maxAbsoluteSum([1, -3, 2, 3, -4])); // Output: 5