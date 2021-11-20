def firstUniqChar(s):
    vals = [-2] * 26
    # -2 doesn't exist
    # -1 repeat

    for idx, ch in enumerate(s):
        chidx = ord(ch) - ord("a")
        if vals[chidx] == -2:
            vals[chidx] = idx
        elif vals[chidx] >= 0:
            vals[chidx] = -1
    ans = None
    for v in vals:
        if v > -1:
            if  ans == None:
                ans = v
            ans = min(ans, v)
    return ans if ans != None else -1

s = "leetcode"
print(firstUniqChar(s))