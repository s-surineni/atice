/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumCount = function(nums) {
    let posCount = 0, negCount = 0;
    for(const val of nums) {
        if (val < 0) {
            negCount++
        } 
        if (val > 0) {
            posCount++
        }

    }
    return Math.max(negCount, posCount)
};