import sys

def find_max_subarray(vals):
    max_arr = - (sys.maxsize)
    # *better could be made better by intializing trk and max_arr to vals[0]
    # starting iteration from second element
    trk = 0
    for vl in vals:
        trk += vl
        trk = max(trk, vl)
        max_arr = max(trk, max_arr)
    return max_arr


vals = int(input().strip())
