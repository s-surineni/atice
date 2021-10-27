def dfs(num, temp, cur, last, res):
    if not num:
        if cur == target:
            res.append(temp)
        return
    for i in range(1, len(num) + 1):
        val = num[:i]
        if i == 1 or (i > 1 and num[0] != "0"):  # prevent "00*" as a number
            dfs(num[i:], temp + "+" + val, cur + int(val), int(val), res)
            dfs(num[i:], temp + "-" + val, cur - int(val), -int(val), res)
            dfs(
                num[i:],
                temp + "*" + val,
                cur - last + last * int(val),
                last * int(val),
                res,
            )


def addOperators(num, target):
    res, target = [], target
    for i in range(1, len(num) + 1):
        if i == 1 or (i > 1 and num[0] != "0"):  # prevent "00*" as a number
            dfs(
                num[i:], num[:i], int(num[:i]), int(num[:i]), res
            )  # this step put first number in the string
    return res


num = "0123"
target = 6
print(addOperators(num, target))
