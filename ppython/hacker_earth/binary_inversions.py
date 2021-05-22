# https://www.hackerearth.com/challenges/competitive/may-circuits-21/algorithm/binary-inversions-cf645357/
def fill_bin_array(siz, zer, inv):
    beg = [0] * (zer - inv)
    mid = [1, 0] * (inv)
    last = [1] * (siz - len(beg) - len(mid))
    arr = beg + mid + last
    for nu in arr:
        print(nu, end=" ")
    print()

# siz, zer, inv = [int(i) for i in input().strip().split()]
print(fill_bin_array(siz, zer, inv))
