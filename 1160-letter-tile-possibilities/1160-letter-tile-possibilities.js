function getLetterPossibilities(curr, tiles, used, res) {
    // add current combination to result set
    res.add(curr);
    // iterate through tiles array to generate combinations
    for (let i = 0; i < tiles.length; i++) {
        if (!used[i]) {
            used[i] = true; // mark tile as used
        // recursively generate combinations by adding current tile to the current combination
        getLetterPossibilities(curr + tiles[i], tiles, used, res);
        used[i] = false; // unmark tile as used
                }

    }
}
var numTilePossibilities = function(tiles) {
    // initialize a set to store unique tile combinations
    const res = new Set();
    // initialize used array to keep track of used tiles
    const used = new Array(tiles.length).fill(false);
    // call recursive function
    getLetterPossibilities("", tiles, used, res);
    return res.size - 1; // subtract 1 to exclude the empty string
};