# https://www.hackerearth.com/challenges/competitive/may-circuits-21/algorithm/binary-inversions-cf645357/
# https://www.hackerearth.com/problem/algorithm/binary-inversions-cf645357/editorial/
def fill_bin_array(siz, zer, inv):
    ones = siz - zer
    if ones * zer < inv:
        print(-1)
        return
    while siz:
        if ones * (zer - 1) >= inv and zer:
            print(0, end=' ')
            zer -= 1
        else:
            print(1, end=' ')
            inv -= zer
            ones -= 1
        siz -= 1

siz, zer, inv = [int(i) for i in input().strip().split()]
fill_bin_array(siz, zer, inv)
