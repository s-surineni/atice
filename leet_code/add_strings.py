from collections import deque

def addStrings(num1, num2):
    num1, num2 = (num1, num2) if len(num1) > len(num2) else (num2, num1)
    res = deque()
    l1 = len(num1)
    l2 = len(num2)
    brow = 0
    su = 0
    dig = 0
    for trk in range(1, l2 + 1):
        su = int(num1[-trk]) + int(num2[-trk]) + brow
        brow = su // 10
        dig = str(su % 10)
        # print(dig, end='')
        res.appendleft(str(dig))
    for trk in range(l2 + 1, l1 + 1):
        su = (int(num1[-trk]) + brow)
        brow = su // 10
        dig = str(su % 10)
        res.appendleft(dig)
    if brow:
        res.appendleft(str(brow))
    return ''.join(res)

print(addStrings("11", "123"))
# addStrings("88", "8")
# addStrings("88", "88")
