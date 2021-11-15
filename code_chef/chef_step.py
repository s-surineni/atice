tc = int(input())

for _ in range(tc):
    dis, step = [int(i) for i in input().split()]
    ans = ''
    for _ in range(dis):
        ans += '1' if not int(input()) % step else '0'
    print(ans)
