def add_strings_recurse(num1, num2, brow):
    if not num2:
        if num1:
            print(num1[:-1], end='')
            print(int(num1[-1]) + brow, end='')
        else:
            print(brow, end='')
        return

    su = 0
    dig = 0

    su = int(num1[-1]) + int(num2[-1]) + brow
    brow = su // 10
    add_strings_recurse(num1[:-1], num2[:-1], brow)
    dig = su % 10
    print(dig, end='')


def addStrings(num1, num2):
    num1, num2 = (num1, num2) if len(num1) > len(num2) else (num2, num1)
    add_strings_recurse(num1, num2, 0)
    print()

addStrings("11", "123")
addStrings("88", "8")
addStrings("88", "88")
