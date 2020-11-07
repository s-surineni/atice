tc = int(input())
for _ in range(tc):
    input()
    times = [int(i) for i in input().split()]
    times.sort(reverse=True)
    # print(times)
    stove1 = 0
    stove2 = 0
    idx = 0
    while idx < len(times):
        if stove1 <= stove2:
            stove1 += times[idx]
        else:
            stove2 += times[idx]
        idx += 1
    print(max(stove1, stove2))
