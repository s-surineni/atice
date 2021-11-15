import heapq


def get_max_soldiers(piers):
    piers = [-1 * ele for ele in piers]
    heapq.heapify(piers)
    print('*' * 80)
    print('iron man piers', piers)
    res = 0
    while piers:
        curr = heapq.heappop(piers)
        res -= curr
        if piers:
            nxt = heapq.heappop(piers)
            if nxt - 1 != curr:
                heapq.heappush(piers, nxt)
    if piers:
        res -= heapq.heappop(piers)
    print('*' * 80)
    print('iron man res', res)
    return res


# piers = [1]
# piers = [1, 2]
# piers = [1, 2, 3]
piers = [1, 3, 5]
print(get_max_soldiers(piers))
