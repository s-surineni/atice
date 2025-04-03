/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumTripletValue = function(nums) {
    const maxSoFarLeft = new Array(nums.length);
    const maxSoFarRight = new Array(nums.length);
    let max = nums[0];
    for (let i = 0; i < nums.length; i++) {
        maxSoFarLeft[i] = max;
        max = Math.max(max, nums[i]);
    }
    max = nums[nums.length - 1];
    for (let i = nums.length - 1; i >= 0; i--) {
        maxSoFarRight[i] = max;
        max = Math.max(max, nums[i]);
    }
    let res = 0;
    for (let idx = 1; idx < nums.length - 1; idx++) {
        res = Math.max(res, (maxSoFarLeft[idx] - nums[idx]) * maxSoFarRight[idx]);
    }
    return res;
};
