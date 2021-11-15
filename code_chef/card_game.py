# https://www.codechef.com/JULY20B/problems/CRDGAME
from functools import reduce


def get_digits_sum(card):
    if int(card) < 10:
        return int(card)
    else:
        return reduce(lambda a, b: int(a) + int(b), card)


tc = int(input().strip())

for _ in range(tc):
    rounds = int(input().strip())
    awin, bwin = 0, 0
    for _ in range(rounds):
        acard, bcard = input().split()
        aval, bval = get_digits_sum(acard), get_digits_sum(bcard)

        if aval > bval:
            awin += 1
        elif aval < bval:
            bwin += 1
        else:
            awin, bwin = awin + 1, bwin + 1

    if awin > bwin:
        print(0, awin)
    elif awin < bwin:
        print(1, bwin)
    else:
        print(2, awin)
