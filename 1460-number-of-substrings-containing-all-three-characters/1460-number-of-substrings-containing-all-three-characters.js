/**
 * @param {string} s
 * @return {number}
 */
var numberOfSubstrings = function(s) {
    let res = 0
    let start = 0, end = 0;
    const charObj = {}
    const wordLen = s.length
    while (end < wordLen) {
        charObj[s[end]] = (charObj[s[end]] || 0) + 1
        while (Object.keys(charObj).length === 3) {
            res += wordLen - end
            charObj[s[start]]--
            if (charObj[s[start]] === 0) {
                delete charObj[s[start]]
            }
            start++
        }
        end++
    }
    return res
};