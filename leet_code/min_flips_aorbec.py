a, b, c = [int(i) for i in input('please enter nums separated by spaces: ').split()]

a = bin(a)[2:][::-1]
b = bin(b)[2:][::-1]
c = bin(c)[2:][::-1]
print(a, b, c)

a, b = (a, b) if len(a) > len(b) else (b, a)
print('a, b', a, b)
len_diff = abs(len(a) - len(b))
b += len_diff * '0'

len_diff = (len(a) - len(c))
if len_diff > 0:
    c += len_diff * '0'
elif len_diff < 0:
    len_diff = abs(len_diff)
    a += len_diff * '0'
    b += len_diff * '0'

print('after', a, b, c)
flips = 0
for idx, dig in enumerate(c):
    if int(dig):
        if not int(a[idx]) and not int(b[idx]):
            flips += 1
    else:
        if int(a[idx]):

            flips += 1
        if  int(b[idx]):
            flips += 1

print(flips)
