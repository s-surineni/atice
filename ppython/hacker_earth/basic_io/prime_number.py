# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/prime-number-8/

n = int(input().strip())

sieve = [True] * (n + 1)

for pr in range(2, n + 1):
    if pr:
        mul = 0
        while (pr ** 2) + (mul * pr) <= n:
            sieve[(pr ** 2) + (mul * pr)] = False
            mul += 1


for pr in range(2, n+ 1):
    if sieve[pr]:
        print(pr, end=' ')
