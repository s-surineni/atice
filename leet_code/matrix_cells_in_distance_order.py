from bisect import insort


def get_maxtrix_cells_in_distance_order(rows, cols, r0, c0):
    result = []

    for rid in range(rows):
        for cid in range(cols):
            curr_dist = abs(rid - r0) + abs(cid - c0)
            insort(result, (curr_dist, (rid, cid)))

    return [k for j, k in result]


if __name__ == '__main__':
    # print(get_maxtrix_cells_in_distance_order(1, 2, 0, 0))
    print(get_maxtrix_cells_in_distance_order(2, 2, 0, 1))
