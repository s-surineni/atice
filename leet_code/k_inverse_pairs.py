def find_k_inverse_pairs_rec(n, k, cache):
    if not n:
        return 0
    if not k:
        return 1
    if cache[n][k] != None:
        return cache[n][k]

    res = 0
    # TODO: think about top-to-bottom by reversing k value from k to 0
    for trk in range(min(n-1, k) + 1):
        res = (res + find_k_inverse_pairs_rec(n -1, k - trk, cache)) % ((10 ** 9) + 7)
    cache[n][k] = res
    return res

def find_k_inverse_pairs(n, k):
    cache = [[None] * (k + 1) for _ in range(n + 1)]
    return find_k_inverse_pairs_rec(n,k, cache)


print(find_k_inverse_pairs(3, 1))
