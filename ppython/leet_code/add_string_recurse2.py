def add_strings_recurse(num1, num2, brow, res):
h    if not num2:
        if num1:
            res.append(num1[:-1])
            su = int(num1[-1]) + brow
            brow = su // 10
            dig = su % 10
            res.append(dig)
        elif brow:
            res.append(brow)
        return

    su = int(num1[-1]) + int(num2[-1]) + brow
    brow = su // 10
    add_strings_recurse(num1[:-1], num2[:-1], brow, res)
    dig = su % 10
    res.append(dig)


def addStrings(num1, num2):
    num1, num2 = (num1, num2) if len(num1) > len(num2) else (num2, num1)
    res = []
    add_strings_recurse(num1, num2, 0, res)
    print(''.join([str(x) for x in res]))

# addStrings("11", "123")
# addStrings("88", "8")
# addStrings("88", "88")
# addStrings("0", "0")
addStrings("6994", "36")
