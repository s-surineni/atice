def convert_postfix_to_infix(expr):
    operators = '*-+/'
    infix = []
    for ch in expr:
        if ch in operators:
            r, l = infix.pop(), infix.pop()
            infix.append('(' + l + ch + r + ')')
        else:
            infix.append(ch)
    return infix.pop()


if __name__ == '__main__':
    expr = ["2", "1", "+", "3", "*"]
    expr = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    print(convert_postfix_to_infix(expr))
