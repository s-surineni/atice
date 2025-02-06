/**
 * @param {number[]} nums
 * @return {number}
 */
var tupleSameProduct = function(nums) {
    // find product of all pairs
    let productMap = {};
    for (let i = 0; i < nums.length; i++) {
        for (let j = i + 1; j < nums.length; j++) {
            const product = nums[i] * nums[j];
            productMap[product] = (productMap[product] || 0) + 1;
        }
    }
    let result = 0;
    for (let key in productMap) {
        if (productMap[key] > 1) {
            result += (productMap[key] * (productMap[key] - 1)) / 2;
        }
    }
    return result * 8;
};