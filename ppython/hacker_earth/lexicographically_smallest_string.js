function minString() {
    s = '<>'
    let letters = "abcdefghijklmnopqrstuvwxyz";
    let res = "";
    s += "<"; // add a stub
    for (let i = 0; i < s.length; i++) {
        if (s[i] === "<") {
            res += letters[i];
        } else {
            let start = i;
            while (s[i] === ">") i++;
            for (let j = i; j >= start; j--) {
                res += letters[j]; // descending series of letters
            }
        }
    }
    return res;
}
console.log(minString())
