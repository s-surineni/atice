def ways(pizza, K: int) -> int:
    m, n, MOD = len(pizza), len(pizza[0]), 10**9 + 7
    preSum = [[0] * (n + 1) for _ in range(m + 1)]
    for r in range(m - 1, -1, -1):
        for c in range(n - 1, -1, -1):
            preSum[r][c] = preSum[r][c + 1] + preSum[r + 1][c] - preSum[r + 1][
                c + 1] + (pizza[r][c] == 'A')
    print('*' * 80)
    print('iron man preSum', preSum)


pizza = ["A..", "AAA", "..."]
cuts = 3
print(ways(pizza, cuts))
