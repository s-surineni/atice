tc = int(input().strip())

for _ in range(tc):
    darth, saber = [int(i) for i in input().strip().split()]
    while darth > 0 and saber:
        darth -= saber
        saber //= 2
    print(1 if darth < 0 else 0)
