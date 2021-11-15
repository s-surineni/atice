import math


def find_coconuts(xa, xb, Xa, Xb):
    xxa = math.ceil(Xa / xa)
    xxb = math.ceil(Xb / xb)
    return xxa + xxb


tc = int(input().strip())
for _ in range(tc):
    inp = [int(i) for i in input().strip().split()]
    print(find_coconuts(*inp))
