/**
 * @param {number[]} nums
 * @return {boolean}
 */
var isArraySpecial = function(nums) {
    if (nums.length == 1) {
        return true;
    }
    let par = nums[0] % 2;
    for (let i = 1; i < nums.length; i++) {
        if (nums[i] % 2 == par) {
            return false;
        }
        par = nums[i] % 2;
    }
    return true;
};