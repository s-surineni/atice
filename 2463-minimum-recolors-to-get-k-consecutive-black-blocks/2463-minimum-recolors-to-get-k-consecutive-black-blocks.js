var minimumRecolors = function(blocks, k) {
    let whiteCount = 0;
    for (let i = 0; i < k; i++) {
        if (blocks[i] === 'W') {
            whiteCount++;
        }
    }
    let res = whiteCount;
    for (let i = k; i < blocks.length; i++) {
        if (blocks[i - k] === 'W') {
            whiteCount--;
        }
        if (blocks[i] === 'W') {
            whiteCount++;
        }
        res = Math.min(res, whiteCount);
    }
    return res;
};