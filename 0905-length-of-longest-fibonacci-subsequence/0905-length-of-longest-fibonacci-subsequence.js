var lenLongestFibSubseq = function(arr) {
    const arrLen = arr.length;
    const mem = new Array(arrLen).fill(0).map(() => new Array(arrLen).fill(0));
    // const temp = new Array(arrLen).map((val) => {
    //     console.log('ironman val', JSON.stringify(val));
    //     return new Array(arrLen).fill(0)});
    // console.log('ironman temp', JSON.stringify(temp));

    // const temp = new Array(arrLen);
    // for (let i = 0; i < arrLen; i++) {
    //     console.log(temp[i])
    // }

    let maxLen = 0
    const valIdx = {}
    for (let i = 0; i < arrLen; i++) {
        valIdx[arr[i]] = i
    }
    for(let i = 1; i < arrLen; i++) {
        for (let j = 0; j < i; j++) {
            const diff = arr[i] - arr[j]
            let currLen = 0
            if (diff < arr[j] && diff in valIdx) {
                currLen = mem[j][valIdx[diff]] + 1
            } else {
                currLen = 2
            }
            mem[i][j] = currLen
            maxLen = Math.max(maxLen, currLen)
        }
    }
    return maxLen > 2 ? maxLen : 0;
};