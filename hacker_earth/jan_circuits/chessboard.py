# https://www.hackerearth.com/challenges/competitive/january-circuits-21/algorithm/chessboard-2-8f06e380/undefined/

def runn():
        k1x, k1y = map(int, input().split())
        k2x, k2y = map(int, input().split())
        if (k1x, k1y) == (k2x, k2y):
            return 'SECOND'
        elif abs(abs(k1x - k2x) + abs(k1y - k2y)) == 1 or abs(k1x - k2x) == abs(k1y - k2y) == 1:
            return 'FIRST'
        else:
            return 'DRAW'

tc = int(input())

for _ in range(tc):
    print(runn())
