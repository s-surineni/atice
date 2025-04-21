var numberOfArrays = function(differences, lower, upper) {
    let minv = 0, maxv = 0, val1 = 0;
    for (let val of differences) {
        let val2 = val + val1;
        minv = Math.min(minv, val2);
        maxv = Math.max(maxv, val2);
        val1 = val2;
    }
    return Math.max(0, (upper - lower) - (maxv - minv) + 1);

};