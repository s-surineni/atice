var applyOperations = function(nums) {
    for (let i = 0; i < nums.length - 1; i ++) {
        if (nums[i] == nums[i + 1]) {
            nums[i] *= 2;
            nums[i + 1] = 0;
        }
    }

    res = new Array(nums.length).fill(0)
    resIdx = 0
    for (const val of nums) {
        if (val !== 0) {
            res[resIdx] = val;
            resIdx ++;
        }
    }
    return res
};