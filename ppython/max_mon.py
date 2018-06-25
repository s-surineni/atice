# https://practice.geeksforgeeks.org/problems/maximum-money/0
tc = int(input().strip())

for trk in range(tc):
    house_mon = input().strip().split()
    house_mon = [int(i) for i in house_mon]
    house, mon = house_mon[0], house_mon[1]
    max_h = house // 2

    if house % 2:
        max_h += 1

    print(max_h * mon)
