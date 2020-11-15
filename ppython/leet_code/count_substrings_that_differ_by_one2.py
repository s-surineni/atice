def count_sub_strs(str1, str2):
    str1_len = len(str1)
    str2_len = len(str2)
    dpl = [[0] * (str1_len + 1) for _ in range(str2_len + 1)]
    dpr = [[0] * (str1_len + 1) for _ in range(str2_len + 1)]

    for idx1, val1 in enumerate(str1):
        for idx2, val2 in enumerate(str2):
            if val1 == val2:
                dpl[idx1 + 1][idx2 + 1] = 1 + dpl[idx1][idx2]

    idx1 = str1_len
    idx2 = str2_len
    while idx1 > 0:
        while idx2 > 0:
            if str1[idx1 - 1] == str2[idx2 - 1]:
                dpr[idx1 - 1][idx2 - 1] = 1 + dpr[idx1][idx2]
            idx2 -= 1
        idx1 -= 1
    res = 0
    for idx1, val1 in enumerate(str1):
        for idx2, val2 in enumerate(str2):
            if val1 != val2:
                res += (dpl[idx1][idx2] + 1) * (dpr[idx1 + 1][idx2 + 1] + 1)
    return res
    # print(dpl)
    # print(dpr)
# str1 = 'aba'
# str2 = 'bab'
str1 = 'ab'
str2 = 'bb'
print(count_sub_strs(str1, str2))
