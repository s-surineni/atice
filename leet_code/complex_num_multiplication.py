def split_nums(comp):
    a, b = comp.split('+')
    b = b[:-1]
    return int(a), int(b)


def complex_num_multiplication(num1, num2):
    a, b = split_nums(num1)
    c, d = split_nums(num2)
    e = (a * c) - (b * d)
    f = (a * d) + (b * c)
    return '{}+{}i'.format(e, f)


num1, num2 = "1+1i", "1+1i"
print(complex_num_multiplication(num1, num2))
