/**
 * @param {number[]} nums
 * @return {number[]}
 */
var buildArray = function(nums) {
     const numLen = nums.length; 
    let res = new Array(numLen);
    for (let i = 0; i < numLen; i++) {
        res[i] = nums[nums[i]]
    }
    return res
};