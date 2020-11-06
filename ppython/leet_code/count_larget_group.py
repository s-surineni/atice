def countLargestGroup(n):
    cots = [0] * (n + 1)
    mem = {0:0}
    for nu in range(1, n + 1):
        qu, rem = divmod(nu, 10)
        mem[nu] = rem + mem[qu]
        cots[mem[nu]] += 1
    return cots.count(max(cots))


n = 21
print(countLargestGroup(n))
