/**
 * @param {number} left
 * @param {number} right
 * @return {number[]}
 */

function findPrimes(limit) {
    const sieve = new Array(limit + 1).fill(true);
    sieve[0] = sieve[1] = false;
    for (let i = 2; i * i <= limit; i++) {
        if (sieve[i]) {
            for (let j = i * i; j <= limit; j += i) {
                sieve[j] = false;
            }
        }
    }
    return sieve;
}
var closestPrimes = function(left, right) {
    const sieve = findPrimes(right)
    const primes = []
    for (let i = left; i <= right; i++) {
        if (sieve[i]) {
            primes.push(i)
        }
    }
    let minDiff = Infinity
    let result = []
    for (let i = 0; i < primes.length - 1; i++) {
        const diff = primes[i + 1] - primes[i]
        if (diff < minDiff) {
            minDiff = diff
            result = [primes[i], primes[i + 1]]
        }
    }
    if (result.length === 0) {
        return [-1, -1]
    }
    return result
};