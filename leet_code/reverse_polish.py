def sub(a, b):
    return a - b


def add(a, b):
    return a + b


def prod(a, b):
    return a * b


def div(a, b):
    return int(a / b)


def evaluate_reverse_polish(expr):
    exp_stack = []

    expressions = {'-': sub,
                   '+': add,
                   '*': prod,
                   '/': div}
    for ch in expr:
        if ch in expressions:
            sec = exp_stack.pop()
            fir = exp_stack.pop()
            exp_stack.append(expressions[ch](fir, sec))
        else:
            exp_stack.append(int(ch))

    return exp_stack[0]


if __name__ == '__main__':
    expr = ["2", "1", "+", "3", "*"]
    expr = ["4", "13", "5", "/", "+"]
    expr = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    print(evaluate_reverse_polish(expr))
