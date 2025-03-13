function canFormZeroArray(nums, queries, mid) {
    const diffArray = new Array(nums.length + 1).fill(0);
    const numsLen = nums.length;
    let totalSum = 0;
    for (let idx = 0; idx < mid; idx ++) {
        const [start, end, val] = queries[idx];
        diffArray[start] += val;
        diffArray[end + 1] -= val;    
    }
    // console.log('ironman diffArray', JSON.stringify(diffArray));
    for (let i = 0; i <= numsLen; i++) {
        totalSum += diffArray[i];
        if (totalSum < nums[i]) {
            return false;
        }
    }
    return true;
}
var minZeroArray = function(nums, queries) {
    let start = 0
    let end = queries.length;
    if (!canFormZeroArray(nums, queries, end)) {
        return -1;
    }
    while (start <= end) {
        let mid = Math.floor((start + end) / 2);
        // let midRes = canFormZeroArray(nums, queries, mid);
        // console.log("midRes", midRes)
        if (canFormZeroArray(nums, queries, mid)) {
            end = mid - 1;
        } else {
            start = mid + 1;
        }
    }
    return start;
};