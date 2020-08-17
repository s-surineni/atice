# https://www.codechef.com/AUG20B/problems/CRDGAME3
tc = int(input().strip())

for _ in range(tc):
    che, ric = [int(i) for i in input().strip().split()]
    ched = che // 9 + (1 if che % 9 else 0)
    ricd = ric // 9 + (1 if ric % 9 else 0)
    print(0 if ched < ricd else 1, end=' ')
    print(ched if ched < ricd else ricd)
