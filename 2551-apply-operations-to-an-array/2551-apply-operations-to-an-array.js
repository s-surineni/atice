var applyOperations = function(nums) {
    for (let i = 0; i < nums.length - 1; i ++) {
        if (nums[i] == nums[i + 1]) {
            nums[i] *= 2;
            nums[i + 1] = 0;
        }
    }
    let nonZeroIdx = 0;
    for (let i = 0; i< nums.length; i++) {
        if(nums[i] != 0) {
            nums[nonZeroIdx] = nums[i];
            nonZeroIdx ++;
        }
    }
    while (nonZeroIdx < nums.length) {
        nums[nonZeroIdx] = 0;
        nonZeroIdx ++;
    }
    return nums;
};