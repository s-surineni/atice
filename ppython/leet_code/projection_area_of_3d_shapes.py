def find_projection_area(matr):
    rlen, clen = len(matr), len(matr[0])
    total_area = 0
    rmax = [0] * rlen
    cmax = [0] * clen

    for rid, row in enumerate(matr):
        for cid, val in enumerate(row):
            if not val:
                continue
            total_area += 1
            if rmax[rid] < val:
                rmax[rid] = val
            if cmax[cid] < val:
                cmax[cid] = val
    total_area += sum(rmax) + sum(cmax)

    return total_area


# matr = [[1, 2], [3, 4]]
matr = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
print(find_projection_area(matr))
