/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var countPairs = function(nums, k) {
    let res = 0;
    for (let idx1 = 0; idx1 < nums.length - 1; idx1++) {
        for (let idx2 = idx1 + 1; idx2 < nums.length; idx2++) {
            if (nums[idx1] === nums[idx2] && (idx1 * idx2) % k === 0) {
                res++;
            }
        }
    }
    return res;
};