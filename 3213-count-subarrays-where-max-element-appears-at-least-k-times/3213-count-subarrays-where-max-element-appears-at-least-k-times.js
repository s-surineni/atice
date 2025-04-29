var countSubarrays = function(nums, k) {
    let [start, end, maxElement, maxEleCount] = [0, 0, 0, 0];
    let res = 0;
    // find max element in the array
    for (let i = 0; i < nums.length; i++) {
        maxElement = Math.max(maxElement, nums[i]);
    }
    while (end < nums.length) {
        if (nums[end] === maxElement) {
            maxEleCount++;
        }
        while (maxEleCount == k) {
            
            if (nums[start] === maxElement) {
                maxEleCount--;
            }
            start++;
        }
        res += start;
        end++;
    }
    return res;
        
};