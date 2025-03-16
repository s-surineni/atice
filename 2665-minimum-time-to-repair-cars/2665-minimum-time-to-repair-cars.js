/**
 * @param {number[]} ranks
 * @param {number} cars
 * @return {number}
 */
var repairCars = function(ranks, cars) {
    let left = 1
    const freqMap = {}
    let minRank = ranks[0], maxRank = 0
    for (const rank of ranks) {
        freqMap[rank] = (freqMap[rank] || 0) + 1
        minRank = Math.min(minRank, rank)
        maxRank = Math.max(maxRank, rank)
    }
    right = minRank * cars * cars
    while (left < right) {
        const mid = Math.floor((left + right) / 2)
        let carsRepaired  = 0
        for (const rank in freqMap) {
            const freq = freqMap[rank]
            const rankRep = Math.floor(Math.sqrt(mid / rank))
            carsRepaired += freq * rankRep
        }
        if (carsRepaired >= cars) {
            right = mid
        } else {
            left = mid + 1
        }
    }
    return left
};

