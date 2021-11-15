def dig_prod(num, dig, idx):
    carry = 0
    dig = int(dig)
    res = []
    num = reversed(num)
    for dig2 in num:
        prod_val = int(dig2) * dig
        prod_val += carry
        rem = prod_val % 10
        carry = int(prod_val // 10)
        res.append(rem)
    if carry:
        res.append(int(carry))
    res = list(reversed(res))
    for _ in range(idx):
        res.append(0)
    print(res)
    return res


def summit(num1, num2):
    carry = 0
    res = []
    if not num2:
        return num1
    for idx in range(1, len(num2) + 1):
        idx = -idx
        summ = num1[idx] + num2[idx]
        summ += carry
        rem = summ % 10
        carry = int(summ // 10)
        res.append(rem)
    if len(num1) != len(num2):
        for idx in range(abs(len(num1) - len(num2))):
            idx = abs(len(num1) - len(num2)) - idx - 1
            summ = num1[idx] + carry
            rem = summ % 10
            carry = int(summ // 10)
            res.append(rem)
    if carry:
        res.append(carry)
    return list(reversed(res))


def multiply_strings(num1, num2):
    if len(num2) < len(num1):
        num1, num2 = num2, num1
    if num1 == "0" or num2 == "0":
        return "0"
    res = []
    for idx, dig in enumerate(reversed(num1)):
        prod = dig_prod(num2, dig, idx)
        res = summit(prod, res)
    res = [str(val) for val in res]
    return "".join(res)


num1 = "99"
num2 = "99"
num1 = "123"
num2 = "456"
num1 = "408"
num2 = "5"
num1 = "140"
num2 = "721"
print(multiply_strings(num1, num2))
