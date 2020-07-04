tc = int(input())

for _ in range(tc):

    total_points, b1, b2 = [int(i) for i in input().strip().split()]
    b1, b2 = b1 - 1, b2 - 1
    tot_triangles = 0
    blacks = {b1, b2}
    for i in range(total_points):
        if i in blacks or i + 1 in blacks:
            continue
        if (i - 1) % total_points in blacks:
            tot_triangles += total_points - 4
        else:
            tot_triangles += total_points - 5
    print(tot_triangles)
