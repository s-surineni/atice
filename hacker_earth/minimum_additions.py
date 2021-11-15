# https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/minimum-additions-0142ac80/

def find_min_addtions(arr, lim):
    wsum = sum(arr)
    arlen = len(arr)
    num_to_add = 0
    while wsum // arlen > lim:
        wsum += 1
        arlen += 1
        num_to_add += 1
    return num_to_add


tc = int(input())
for _ in range(tc):
    n, lim = [int(i) for i in input().split()]
    arr = [int(i) for i in input().split()]
    print(find_min_addtions(arr, lim))
