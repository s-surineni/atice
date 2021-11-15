tc = int(input())

for _ in range(tc):
    input()
    strins = [int(i) for i in input().split()]

    skips = 0
    for s1, s2 in zip(strins, strins[1:]):
        skips += abs(s1 - s2) - 1
    print(skips)
