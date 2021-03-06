def longestDecomposition(S, res=0):
    n = len(S)
    for l in range(1, n //2 + 1):
        if S[0] == S[n - l] and S[l - 1] == S[n - 1]:
            if S[:l] == S[n - l:]:
                return longestDecomposition(S[l:n - l], res + 2)
    return res + 1 if S else res


longestDecomposition("ghiabcdefhelloadamhelloabcdefghi")
