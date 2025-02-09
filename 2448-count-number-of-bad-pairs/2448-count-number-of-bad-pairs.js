var countBadPairs = function(nums) {
    const idxValCount = {};
    let badPairs = 0;
    for (let i = 0; i < nums.length; i++) {
        const idxVal = i - nums[i];
        let goodPairs = idxValCount[idxVal] || 0;
        badPairs += i - goodPairs;
        idxValCount[idxVal] = (idxValCount[idxVal] || 0) + 1;
    }
    return badPairs;
};