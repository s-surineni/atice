def dfs(rlen, clen, cuts, rrr, ccc, suff_sum, cach):
    mod = 10 ** 9 + 7
    if not suff_sum[rrr][ccc]: return 0
    if not cuts: return 1
    if cach[rrr][ccc][cuts]:
        return cach[rrr][ccc][cuts]
    ans = 0
    for ridx in range(rrr + 1, rlen):
        if suff_sum[rrr][ccc] - suff_sum[ridx][ccc] > 0:
            ans += dfs(rlen, clen, cuts - 1, ridx, ccc, suff_sum, cach)

    for cidx in range(ccc + 1, clen):
        if suff_sum[rrr][ccc] - suff_sum[rrr][cidx]:
            ans += dfs(rlen, clen, cuts - 1, rrr, cidx, suff_sum, cach)

    cach[rrr][ccc][cuts] = ans
    return ans % mod


def find_ways_of_cutting_pizza(pizza, cuts):
    rlen = len(pizza)
    clen = len(pizza[0])
    suff_sum = [[0] * (clen + 1) for _ in range(rlen + 1)]
    # print(suff_sum)

    cach = [[[0] * (cuts) for _ in range(clen)] for _ in range(rlen)]
    # print('*' * 80)
    # print('iron man cach', cach)
    ridx = rlen

    while ridx > 0:
        cidx = clen
        while cidx > 0:
            # print('*' * 80)
            # print('iron man ridx, cidx', ridx, cidx)
            piz = 1 if pizza[ridx - 1][cidx - 1] == 'A' else 0
            suff_sum[ridx - 1][cidx - 1] = (suff_sum[ridx - 1][cidx]
                                            + suff_sum[ridx][cidx - 1]
                                            - suff_sum[ridx][cidx]
                                            + piz)
            cidx -= 1
        ridx -= 1
    # print(suff_sum)
    return dfs(rlen, clen, cuts - 1, 0, 0, suff_sum, cach)


# pizza = ["A..", "AAA", "..."]
# cuts = 3

pizza = [".A","AA","A."]
cuts = 3
print(find_ways_of_cutting_pizza(pizza, cuts))
