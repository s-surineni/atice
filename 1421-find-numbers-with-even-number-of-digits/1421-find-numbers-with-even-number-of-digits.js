/**
 * @param {number[]} nums
 * @return {number}
 */
function findDitCount(num) {
    let digCount = 0;
    while (num > 0) {
        digCount++;
        num = Math.floor(num / 10);
    }
    return digCount;
}
var findNumbers = function(nums) {
    let res = 0;
    for (const num of nums) {
        if (findDitCount(num) % 2 == 0) {
            res++;
        }
    }
    return res;
};