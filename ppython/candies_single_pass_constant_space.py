ratings = [int(i) for i in input().split()]

if not ratings:
    res =  0

candies = 0
up = 0
down = 0
old_slope = 0

def candy_count(n):
    return (n * (n + 1)) // 2


for idx in range(1, len(ratings)):
    new_slope = ratings[idx] - ratings[idx - 1]
    print('old_slope', 'new_slope', 'candies')
    print(old_slope, new_slope, candies)
    if (old_slope > 0 and new_slope == 0) or (old_slope < 0 and new_slope >= 0):
        candies += candy_count(up) + candy_count(down) + max(up, down)
        up = down = 0
    if new_slope > 0:
        up += 1
    if new_slope < 0:
        down += 1
    if new_slope == 0:
        candies += 1
    print('up', 'down')
    print(up, down)
    old_slope = new_slope

print('up', 'down')
print(up, down)
print('candies ', candies)
candies += candy_count(up) + candy_count(down) + max(up, down) + 1
print(candies)
