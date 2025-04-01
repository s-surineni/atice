function mostPointsRecur(index, questions, cache) {
    if (index >= questions.length) {
        return 0;
    }
    if (cache[index] !== -1) {
        return cache[index];
    }
    let res = Math.max(questions[index][0] + mostPointsRecur(index + questions[index][1] + 1, questions, cache), mostPointsRecur(index + 1, questions, cache));
    cache[index] = res;
    return res;
}
/**
 * @param {number[][]} questions
 * @return {number}
 */
var mostPoints = function(questions) {
    // initialize cache array
    const cache = new Array(questions.length).fill(-1);
    // define recursive function to calculate the maximum points
    return mostPointsRecur(0, questions, cache);
};