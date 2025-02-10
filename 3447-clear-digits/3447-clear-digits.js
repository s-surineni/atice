/**
 * @param {string} s
 * @return {string}
 */
var clearDigits = function(s) {
    // initialize a stack
    let stack = [];
    // loop through the string
    for (const char of s) {
        // if the character is a digit
        if (char >= '0' && char <= '9') {
            // pop the stack
            stack.pop();
        } else {
            // push the character to the stack
            stack.push(char);
        }
    }
    // return the stack joined
    return stack.join('');
};