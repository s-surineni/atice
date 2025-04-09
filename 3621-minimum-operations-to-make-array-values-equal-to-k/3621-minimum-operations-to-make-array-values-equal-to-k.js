/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var minOperations = function(nums, k) {
    let numDict = {};
    let ops = 0;
    for (const aNum of nums) {
        if (aNum < k) {
            return -1;
        } else if (!(aNum in numDict) && aNum != k) {
            ops++;
            numDict[aNum] = 1;
        }
    }
    return ops;
};