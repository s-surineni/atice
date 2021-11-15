# https://www.codechef.com/OCT20B/problems/CHEFEZQ
tc = int(input().strip())


for _ in range(tc):
    days, limit = [int(i) for i in input().strip().split()]

    query_cumu = 0
    for idx, queries in enumerate([int(i) for i in input().strip().split()]):
        query_cumu += queries - limit
        if query_cumu < 0:
            print(idx + 1)
            break
    else:
        print(idx + 2 + query_cumu // limit)
