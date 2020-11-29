def fun(s, z):
    total = 0
    len_str = len(s)

    for x, y in z:
        if x == 0:
            total += y
        else:
            total -= y
    total = total % len_str
    return s[total:] + s[:total]



print(fun('cutshort', [[0, 3], [1, 11]]))
