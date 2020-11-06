def find_lcs(astr, bstr):
    mem = [[""] * (len(astr) + 1) for _ in range(len(bstr) + 1)]
    for bi, bs in enumerate(bstr):
        for ai, ar in enumerate(astr):
            if bs != ar:
                mem[bi + 1][ai + 1] = max(mem[bi + 1][ai],
                                          mem[bi][ai + 1],
                                          key=len)
            else:
                mem[bi + 1][ai +
                            1] = max(mem[bi][ai], mem[bi][ai], key=len) + bs
    # print(mem)
    return mem[-1][-1]


astr = 'abcdaf'
bstr = 'acbcf'
astr = "aaaaaaaa"
bstr = "aaaaaaaa"


def find_shortest_common_supersequence(astr, bstr):
    lcs = find_lcs(astr, bstr)
    res = ''
    ai = bi = 0
    for ch in lcs:
        while astr[ai] != ch:
            res += astr[ai]
            ai += 1
        while bstr[bi] != ch:
            res += bstr[bi]
            bi += 1
        res += ch
        ai += 1
        bi += 1
    res += astr[ai:] + bstr[bi:]
    return res


str1 = "abac"
str2 = "cab"
str1 = "aaaaaaaa"
str2 = "aaaaaaaa"
print(find_shortest_common_supersequence(str1, str2))
