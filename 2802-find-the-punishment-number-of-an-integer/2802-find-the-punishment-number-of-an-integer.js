// 2698. Find the Punishment Number of an Integer
/**
 * @param {number} n
 * @return {number}
 */
var punishmentNumber = function(n) {
    // loop to generate numbers in the range 1 to n
    let res = 0; // variable to store the sum of punishment numbers
    for (let candNum = 1; candNum <= n; candNum++) {
        // calculate the square of the number and convert it to a string
        // console.log('ironman n', JSON.stringify(candNum));
        let square = (candNum * candNum).toString();
        // initialize 2d memoization array of size square.length x i + 1to store the results of subproblems
        const memo = [];
        for (let j = 0; j < square.length; j++) {
            memo.push(new Array(candNum + 1).fill(-1));
        }
        // console.log('ironman memo', JSON.stringify(memo));
        // check if the square is a punishment number using a helper function and add it to the sum if it is
        if (hasValidPartition(0, 0, square, candNum, memo)) {
            res += candNum * candNum;
        }
        // helper function to check if a number is a punishment number using recursion and backtracking
        function hasValidPartition(st_idx, curr_sum, square, target, memo) {
            // check if partition is valid
            if (st_idx === square.length) {
                return curr_sum === target;
            }
            // check for invalid partition
            if (curr_sum > target) {
                return false;
            }
            // check if result is already computed for the current state and return it
            if (memo[st_idx][curr_sum] !== -1) {
                return memo[st_idx][curr_sum];
            }
            partitionFound = false;
            // iterate over the string and try to form a valid partition by adding digits to the current sum
            for (let i = st_idx; i < square.length; i++) {
                curr_string = square.substring(st_idx, i + 1);
                curr_num = parseInt(curr_string);
                partitionFound = partitionFound || hasValidPartition(i + 1, curr_sum + curr_num, square, target, memo);
                // if partition is found, break the loop and return true
                if (partitionFound) {
                    memo[st_idx][curr_sum] = true;
                    return true;
                }
                // if partition is not found, continue to the next iteration
            }
            // if no valid partition is found, return false and store the result in memo
            memo[st_idx][curr_sum] = false;
            return false;
        }
    }
    return res;
};