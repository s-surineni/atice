function generateBinaryString(currIdx, currString, numSet) {
    if (currIdx === numSet.size) {
        if (!numSet.has(currString)) {
            return currString;
        }
        return null;
    }
    // Try appending '0' to the current string and recurse
    let result = generateBinaryString(currIdx + 1, currString + '0', numSet);
    if (result !== null) {
        return result;
    }
    // Try appending '1' to the current string and recurse
    result = generateBinaryString(currIdx + 1, currString + '1', numSet);
    return result;
}
var findDifferentBinaryString = function (nums) {
    // convert nums to set
    let numSet = new Set(nums);
    // call recursive function to generate binary string of length nums.length
    return generateBinaryString(0, "", numSet);
};