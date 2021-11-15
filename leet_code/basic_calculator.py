# https://leetcode.com/problems/basic-calculator
def calculate_number(expr):
    stack = []
    res = 0
    num = 0
    sign = 1

    for ch in expr:
        if ch == "+":
            res += sign * num
            num = 0
            sign = 1
        elif ch == "-":
            res += sign * num
            num = 0
            sign = -1
        elif ch == "(":
            stack.append(res)
            stack.append(sign)
            sign = 1
            res = 0
        elif ch == ")":
            res += sign * num
            num = 0
            res *= stack.pop()
            res += stack.pop()
        elif ch.isdigit():
            num = (num * 10) + int(ch)
    if num:
        res += sign * num
    return res


# s = "1 + 1"
# s = "1 + 2 - 3"
# s = "1 + 12 - 33"
s = "(1+(4+5+2)-3)+(6+8)"
print(calculate_number(s))
