names1 = [3, 31, 34, 4, 2]
names2 = names1
sm = 0
for ls in (names2, names1):
    print(ls)
    print(sum(ls))
    if sum(ls) % 2 == 0:
        sm += 11
if sum(ls) % 4 == 0:
    sm += 10

print(sm)
