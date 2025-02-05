var areAlmostEqual = function(s1, s2) {
    const s1Len = s1.length;
    const s2Len = s2.length;
    if (s1Len !== s2Len) return false;
    let diffCount = 0;
    const s1Chars = {};
    const s2Chars = {};
    for (let i = 0; i < s1Len; i++) {
        if (s1[i] !== s2[i]) {
            diffCount++;
        }
        s1Chars[s1[i]] = (s1Chars[s1[i]] || 0) + 1;
        s2Chars[s2[i]] = (s2Chars[s2[i]] || 0) + 1;
    }
    // compare if the characters are the same
    for (let key in s1Chars) {
        if (s1Chars[key] !== s2Chars[key]) return false;
    }
    for (let key in s2Chars) {
        if (s1Chars[key] !== s2Chars[key]) return false;
    }
    return diffCount <= 2;
};