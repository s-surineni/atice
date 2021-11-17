# https://leetcode.com/problems/unique-paths/
"""
# TODO see how this is wrong
def find_unique_path_recur(currr, currc, endr, endc, res, cache):
    if (currr, currc) in cache:
        return res + cache[(currr, currc)]
    if currr == (endr - 1) and currc == (endc - 1):
        return res + 1
    if currr + 1 < endr:
        res = find_unique_path_recur(currr + 1, currc, endr, endc, res, cache)
    if currc + 1 < endc:
        res = find_unique_path_recur(currr, currc + 1, endr, endc, res, cache)
    cache[(currr, currc)] = res
    return res


def find_unique_path(m, n):
    return find_unique_path_recur(0, 0, m, n, 0, {})

"""

"""
def find_unique_path(rc, cc):
    cache = [[0] * cc for _ in range(rc)]
    for idx in range(rc):
        cache[idx][0] = 1
    for idx in range(cc):
        cache[0][idx] = 1
    for rid in range(1, rc):
        for cid in range(1, cc):
            cache[rid][cid] = cache[rid][cid - 1] + cache[rid - 1][cid]
    return cache[rc - 1][cc - 1]
"""


"""
def find_unique_path(rc, cc):
    pre = [1] * cc
    cur = [0] * cc
    cur[0] = 1

    for rid in range(1, rc):
        for cid in range(1, cc):
            cur[cid] = cur[cid - 1] + pre[cid]
        pre = cur
        cur[0] = 1
    return pre[cc - 1]
"""


# TODO: see an example of how 2 row as being reduced to 1 row
def find_unique_path(rc, cc):
    cur = [1] * cc

    for rid in range(1, rc):
        for cid in range(1, cc):
            cur[cid] += cur[cid - 1]

    return cur[cc - 1]


m = 3
n = 7
# m, n = 1, 2
print(find_unique_path(m, n))
