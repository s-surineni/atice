def count_sub_strs(str1, str2):
    res = 0
    for i in range(len(str1)):
        for j in range(len(str2)):
            miss, pos = 0, 0
            while i + pos < len(str1) and j + pos < len(str2) and miss < 1:
                miss += str1[i + pos] != str2[j + pos]
                res += miss == 1
                pos += 1
    return res


# str1 = 'aba'
# str2 = 'bab'
str1 = 'ab'
str2 = 'bb'
print(count_sub_strs(str1, str2))
