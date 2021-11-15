import sys

tc = int(input().strip())

for _ in range(tc):
    opp, pos = [int(i) for i in input().strip().split()]
    opp_pos = [int(i) for i in input().strip().split()]
    closest = -1
    closest_dist = sys.maxsize

    for a_o in opp_pos:
        if not pos % a_o:
            curr_dist = pos / a_o
            if closest_dist > curr_dist:
                closest = a_o
                closest_dist = curr_dist
    print(closest)
