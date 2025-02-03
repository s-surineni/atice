var longestMonotonicSubarray = function(nums) {
    const numLen = nums.length;
    let maxLen = 1;
    let currLen = 1;
    for (let idx = 0; idx < numLen - 1; idx++) {
        if (nums[idx] < nums[idx + 1]) {
            currLen++;
        } else {
            maxLen = Math.max(maxLen, currLen);
            currLen = 1;
        }
    }
    maxLen = Math.max(maxLen, currLen);
    currLen = 1;
    for (let idx = 0; idx < numLen - 1; idx++) {
        if (nums[idx] > nums[idx + 1]) {
            currLen++;
        } else {
            maxLen = Math.max(maxLen, currLen);
            currLen = 1;
        }
    }
    maxLen = Math.max(maxLen, currLen);
    return maxLen;
};