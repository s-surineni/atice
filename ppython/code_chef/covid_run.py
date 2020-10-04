# https://www.codechef.com/OCT20B/problems/CVDRUN
tc = int(input().strip())


def solve():
    city_count, hop_dist, start, melive = [int(i)
                                           for i in input().strip().split()]
    # <!TODO> see why this is a failure
    # if city_count % 2:
    #     return 'YES'
    curr_city = (start + hop_dist) % city_count
    while curr_city != melive and curr_city != start:
        curr_city = (curr_city + hop_dist) % city_count
    return 'YES' if curr_city == melive else 'NO'


for _ in range(tc):
    print(solve())
