def find_projection_area(matr):
    rlen, clen = len(matr), len(matr[0])
    total_area = 0

    for rid, row in enumerate(matr):
        rmax = 0
        cmax = 0
        for cid, val in enumerate(row):
            if val:
                # continue
                total_area += 1
            # because we are accessing by row be can directly get
            # max value for a row after inner loop
            rmax = max(rmax, val)
            # by switching cid and rid places we are traversing a column
            # also problem statement says its n x n matrix always
            cmax = max(cmax, matr[cid][rid])

        total_area += rmax + cmax

    return total_area


# matr = [[1, 2], [3, 4]]
# matr = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
matr = [[1, 0], [5, 4]]
print(find_projection_area(matr))
