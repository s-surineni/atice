def digits_count(n):
    counter = 0

    while n != 0:
        n //= 10
        counter += 1

    return counter

def func(n, digits = None):    
    if digits is None:
        digits = digits_count(n)

    if digits == 1:
        print('*' * 80)
        print('result', [str(i) for i in range(10)])
        return [str(i) for i in range(10)]

    result = []

    res = func(n, digits - 1)
    result.extend(res)

    for c in [str(i) for i in range(1, 10)]:
        for r in res:
            if abs(int(c) - int(r[0])) == 1 and len(r) == digits - 1:
                num = c + r
                if int(num) > n:
                    return result
                else:
                    result.append(num)

            if int(c) == 1 and len(r) == digits - 2 and int(r[0]) == 1:
                num = c + '0' + r
                if int(num) > n:
                    return result
                else:
                    result.append(num)
    print('result', result)
    return result


tests = int(input().strip())

for _ in range(tests):

    n = int(input().strip())
    result = func(n)[10:]
    print('*' * 80)
    print('result', result)
    if result:
        print(" ".join(result))
    else:
        print(-1)
