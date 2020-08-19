# piers = [1, 2]
# piers = [1, 2, 3]
# piers = [5]
piers = [5, 1]


def get_max_soldiers(piers):
    piers = sorted(piers, reverse=True)
    print('*' * 80)
    print('iron man piers', piers)
    idx = 0
    pier_len = len(piers)
    res = 0
    while idx < (pier_len - 1):
        curr = piers[idx]
        nxt = piers[idx + 1]
        res += curr
        if nxt + 1 == curr:
            idx += 2
        else:
            idx += 1
    if idx == (pier_len - 1):
        res += piers[idx]
    return res


print(get_max_soldiers(piers))
