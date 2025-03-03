/**
 * @param {number[]} nums
 * @param {number} pivot
 * @return {number[]}
 */
var pivotArray = function(nums, pivot) {
    const arrLen = nums.length;
    let bIdx = arrLen - 1;
    let res = new Array(arrLen);
    let step = 0;
    let lowIdx = 0, highIdx = arrLen - 1;
    while (step < arrLen) {
        if (nums[step] < pivot) {
            res[lowIdx] = nums[step];
            lowIdx++;
        }
        if (nums[bIdx - step] > pivot) {
            res[highIdx] = nums[bIdx - step];
            highIdx--;
        }
        step++;
    }
    while (lowIdx <= highIdx) {
        res[lowIdx] = pivot;
        lowIdx++;
    }
    return res;
    
};