function findSmallestNumber(currIdx, pattern, usedNums, currNum) {
    if (currIdx === pattern.length+ 1) {
        // base case: if we have used all digits, return the current number
        return currNum;
    }
    let res = Infinity;
    for (let i = 1; i <= 9; i++) {
        if ((usedNums & (1 << i)) === 0) {
            // if the current digit is not used yet
            const lastDigit = currNum % 10;
            if (currIdx === 0 || pattern[currIdx - 1] === 'I' && i > lastDigit) {
                res = Math.min(res, findSmallestNumber(currIdx + 1, pattern, usedNums | (1 << i), currNum * 10 + i));
            } else if (pattern[currIdx - 1] === 'D' && i < lastDigit) {
                res = Math.min(res, findSmallestNumber(currIdx + 1, pattern, usedNums | (1 << i), currNum * 10 + i));
            }
        }
    }
    return res;
}
var smallestNumber = function(pattern) {
    // call recursive function
    // let currRes = 0;
    return String(findSmallestNumber(0, pattern, 0, 0))
};