var numOfSubarrays = function(arr) {
    arr = arr.map((x) => x % 2);
    const MOD = 1e9 + 7;
    const arrLen = arr.length;
    const oddArr = new Array(arrLen).fill(0);
    const eveArr = new Array(arrLen).fill(0);
    idx = arrLen - 1;
    oddArr[idx] = arr[idx];
    eveArr[idx] = 1 - arr[idx];
    idx--;
    while (idx >= 0) {
        if (arr[idx] === 1) {
            oddArr[idx] = eveArr[idx + 1] + 1;
            eveArr[idx] = oddArr[idx + 1];
        } else {
            oddArr[idx] = oddArr[idx + 1];
            eveArr[idx] = eveArr[idx + 1] + 1;
        }
        idx--;
    }
    let res = 0;
    for (let i = 0; i < arrLen; i++) {
        res += oddArr[i];
        res %= MOD;
    }
    return res;
};