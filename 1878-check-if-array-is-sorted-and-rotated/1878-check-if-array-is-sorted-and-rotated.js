/**
 * @param {number[]} nums
 * @return {boolean}
 */
var check = function(nums) {
    let breaks = 0;
    for (let i = 0; i < nums.length - 1; i++) {
        if (nums[i] > nums[i + 1]) {
            breaks++;
            if (breaks > 2) {
                return false;
            }
        }
    }
    if (nums[0] < nums.at(-1)) {
        breaks++;
    }
    return breaks <= 1;
};