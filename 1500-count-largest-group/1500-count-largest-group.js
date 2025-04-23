/**
 * @param {number} n
 * @return {number}
 */
function findDigitSum(num) {
    let sum = 0;
    while (num > 0) {
        sum += num % 10;
        num = Math.floor(num / 10);
    }
    return sum;
}
var countLargestGroup = function(n) {
    let valMap = new Map();
    for (let i = 1; i <= n; i++) {
        let sum = findDigitSum(i);
        if (valMap.has(sum)) {
            valMap.set(sum, valMap.get(sum) + 1);
        } else {
            valMap.set(sum, 1);
        }
    }
    let maxCount = 0;
    for (let count of valMap.values()) {
        maxCount = Math.max(maxCount, count);
    }
    let result = 0;
    for (let count of valMap.values()) {
        if (count === maxCount) {
            result++;
        }
    }
    return result;
};