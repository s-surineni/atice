import bisect
from collections import defaultdict

def find_most_popular():
    shop_count, pep_count = [int(i) for i in input().split()]
    shop_visits = [0] * shop_count
    # max_visits = 0

    # max_shops = []
    
    for _ in range(pep_count):
        start, end = [int(i) - 1 for i in input().split()]
        
        for sid in range(start, end + 1):
            shop_visits[sid] += 1
            # if max_visits < shop_visits[sid]:
            #     max_shops = [sid]
            #     max_visits2 = max_visits
            #     max_visits = shop_visits[sid]
            # elif max_visits == shop_visits[sid]:
            #     bisect.insort(max_shops, sid)
        # print(shop_visits)

    count_dict = defaultdict(list)
    for k, v in enumerate(shop_visits):
        count_dict[v].append(k)
    print(count_dict)
    shop_visits.sort()
    print('shot visits', shop_visits)
    most_freq = [None] * 3
    for idx in range(2, -1, -1):
        most_freq[idx] = count_dict[shop_visits.pop()].pop(0) + 1
    return most_freq
    
tc = int(input())

for _ in range(tc):
    print(find_most_popular())
