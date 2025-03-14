function canDistribute(candies, k, pileSize) {
    let possiblePiles = 0;
    for (cands of candies) {
        possiblePiles += Math.floor(cands / pileSize)
        if (possiblePiles >= k) {
            return true;
        }
    }
    return false;
}
/**
 * @param {number[]} candies
 * @param {number} k
 * @return {number}
 */
var maximumCandies = function (candies, k) {
    let maxVal = Math.max(...candies);
    // console.log('ironman maxVal', JSON.stringify(maxVal));
    let minVal = 0;
    while (minVal < maxVal) {
        let midVal = Math.floor((minVal + maxVal + 1) / 2);
        if (canDistribute(candies, k, midVal)) {
            minVal = midVal;
        } else {
            maxVal = midVal - 1;
        }
    }
    return minVal;
};