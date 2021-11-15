tc = int(input().strip())

for _ in range(tc):
    cuts = int(input().strip())
    print(((cuts ** 2) + cuts + 2) // 2)
