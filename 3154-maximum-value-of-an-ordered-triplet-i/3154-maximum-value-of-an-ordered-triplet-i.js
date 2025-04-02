/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumTripletValue = function(nums) {
    let t1 = nums[0];
    let res = 0;
    for (let t2 = 1; t2 < nums.length - 1; t2++) {
        for (let t3 = t2 + 1; t3 < nums.length; t3++) {
            res = Math.max(res, (t1 - nums[t2]) * (nums[t3]));
        }
        t1 = Math.max(t1, nums[t2]);
    }
    return res;
};

let nums = [12,6,1,2,7]
console.log(maximumTripletValue(nums)); // Output: 77