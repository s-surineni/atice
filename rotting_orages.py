from collections import deque

def find_time_to_rot(orange_box):
    rows = len(orange_box)
    cols = len(orange_box[0])

    locs = deque()
    for rid, row in enumerate(orange_box):
        for cid, val in enumerate(row):
            if val == 2:
                locs.append((rid, cid, 0))
                break
        if locs:
            break

    while locs:
        c_rid, c_cid, tim = locs.popleft()
        for n_rid, n_cid in [(c_rid - 1, c_cid), (c_rid, c_cid - 1),
                             (c_rid + 1, c_cid), (c_rid, c_cid + 1)]:
            if 0 <= n_rid < rows and 0 <= n_cid < cols:
                if orange_box[n_rid][n_cid] == 1:
                    orange_box[n_rid][n_cid] = 2
                   # <!note> by adding third attribute we are able to track time taken easily
                   # else it would have been difficult to find out current layer in bfs
                    locs.append((n_rid, n_cid, tim + 1))

    for rid, row in enumerate(orange_box):
        for cid, val in enumerate(row):
            if val == 1:
                return -1
    return tim


if __name__ == '__main__':
    orange_box = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    print(find_time_to_rot(orange_box))
