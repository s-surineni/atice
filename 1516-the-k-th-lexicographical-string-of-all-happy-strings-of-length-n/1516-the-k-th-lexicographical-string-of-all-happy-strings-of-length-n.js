function generateHappyString(currIdx, currSeq, lent, res) {
    // base case. when currIx is equal to lent add curr sequence to res
    if (currIdx === lent) {
        res.push(currSeq.join(''));
    }
    if (currIdx > lent) return;
    // if currIdx is not equal to lent then we need to add a, b or c to currSeq
    for (let ch of "abc") {
        if (currIdx === 0 || ch !== currSeq[currIdx - 1]) {
            generateHappyString(currIdx + 1, currSeq.concat([ch]), lent, res);
        }
    }
}
var getHappyString = function(n, k) {
    // call recursive function
    const res = [];
    generateHappyString(0, [], n, res)
    return k <= res.length ?res[k - 1]: ""
};