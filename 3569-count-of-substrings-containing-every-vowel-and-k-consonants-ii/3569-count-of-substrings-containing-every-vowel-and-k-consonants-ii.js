/**
 * @param {string} word
 * @param {number} k
 * @return {number}
 */
function findNextCons(word) {
    const wordLen = word.length;
    const nextConsArr = new Array(wordLen).fill(wordLen);
    let nextCons = wordLen;
    const vowSet = new Set(['a', 'e', 'i', 'o', 'u']);
    for (let i = wordLen - 1; i >= 0; i--) {
        nextConsArr[i] = nextCons;
        if (!vowSet.has(word[i])) {
            nextCons = i;
        }
    }
    return nextConsArr;
}


var countOfSubstrings = function (word, k) {
    const nextCons = findNextCons(word);
    // console.log('ironman nextCons', JSON.stringify(nextCons));
    const vowDict = {};
    let consonantCount = 0;
    let result = 0;
    const wordLen = word.length;
    let start = 0, end = 0;
    const vowSet = new Set(['a', 'e', 'i', 'o', 'u']);
    while (end < wordLen) {
        if (vowSet.has(word[end])) {
            vowDict[word[end]] = (vowDict[word[end]] || 0) + 1;
        } else {
            consonantCount++;
        }
        if (consonantCount === k && Object.keys(vowDict).length === 5) {
            while (consonantCount === k && Object.keys(vowDict).length === 5) {
            result += nextCons[end] - end;

                if (vowSet.has(word[start])) {
                    vowDict[word[start]]--;
                    if (vowDict[word[start]] === 0) {
                        delete vowDict[word[start]];
                    }
                } else {
                    consonantCount--;
                }
                start++;
                // result += nextCons[end] - end;
            }
        } else if (consonantCount > k) {
            while (consonantCount > k) {
                if (vowSet.has(word[start])) {
                    vowDict[word[start]]--;
                    if (vowDict[word[start]] === 0) {
                        delete vowDict[word[start]];
                    }
                } else {
                    consonantCount--;
                }
                start++;
            }
        }
        end++;
    }
    return result;
};