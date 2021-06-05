def find_max_area(hei, wid, hcuts, vcuts):
    hcuts.sort()
    vcuts.sort()

    max_h = hcuts[0]

    for idx, cut in enumerate(hcuts[1:]):
        max_h = max(max_h, cut - hcuts[idx])

    max_h = max(max_h, hei - hcuts[-1])


    max_v = vcuts[0]

    for idx, cut in enumerate(vcuts[1:]):
        max_v = max(max_v, cut - vcuts[idx])

    max_v = max(max_v, wid - vcuts[-1])

    return abs(max_h * max_v)


h = 5
w = 4
horizontalCuts = [1, 2, 4]
verticalCuts = [1, 3]
print(find_max_area(h, w, horizontalCuts, verticalCuts))
