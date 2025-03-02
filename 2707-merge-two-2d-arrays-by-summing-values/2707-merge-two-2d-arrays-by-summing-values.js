var mergeArrays = function(nums1, nums2) {
    let idx1 = 0, idx2 = 0;
    if (nums2.length > nums1.length) {
        [nums1, nums2] = [nums2, nums1];
    }
    const rest = [];
    while (idx1 < nums1.length && idx2 < nums2.length) {
        const [id1, val1] = nums1[idx1];
        const [id2, val2] = nums2[idx2];
        if (id1 == id2) {
            rest.push([id1, val1 + val2]);
            idx1++;
            idx2++;
        } else if (id1 < id2) {
            rest.push([id1,val1]);
            idx1++;
        } else {
            rest.push([id2, val2]);
            idx2++;
        }
    }
    rest.push(...nums1.slice(idx1));
    rest.push(...nums2.slice(idx2));
    return rest;
};

let nums1 = [[1,2],[2,3],[4,5]], nums2 = [[1,4],[3,2],[4,1]];
console.log(mergeArrays(nums1, nums2));