/**
 * @param {number} n
 * @return {string}
 */
var countAndSayRecur = function(n) {
    let curIdx = 0;
    let strLen = n.length;
    let res = [];
    while (curIdx < strLen) {
        const currCh = n[curIdx];
        let nextIdx = curIdx + 1;
        while (nextIdx < strLen && n[nextIdx] === currCh) {
            nextIdx++;
        }
        const count = nextIdx - curIdx;
        res.push(count);
        res.push(currCh);
        curIdx = nextIdx;
    }
    return res.join('');
};
var countAndSay = function(n) {
    let res = '1';
    if (n === 1) {
        return res;
    }
    for (let i = 2; i <= n; i++) {
        res = countAndSayRecur(res);
    }
    return res;
};