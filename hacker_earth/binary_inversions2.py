# https://www.hackerearth.com/challenges/competitive/may-circuits-21/algorithm/binary-inversions-cf645357/
def fill_bin_array(siz, zer, inv):
    if zer > 1:
        print(0, end=' ')
        siz -= 1
        zer -= 2
        for _ in range(inv):
            print(1, end=' ')
            siz -= 1
            if zer:
                print(0, end=' ')
                siz -= 1
        print(0, end=' ')
        siz -= 1
        while siz:
            print(1, end=' ')
            siz -= 1
    else:
        for _ in range(inv):
            print(1, end=' ')
            siz -= 1
        print(0, end=' ')
        siz -= 1
        while siz:
            print(1, end=' ')
            siz -= 1
siz, zer, inv = [int(i) for i in input().strip().split()]
(fill_bin_array(siz, zer, inv))
