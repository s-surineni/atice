from collections import deque


def find_matrix_val(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    bit_vector = 0
    for rid, a_row in enumerate(matrix):
        for cid, a_col in enumerate(a_row):
            if a_col:
                bit_vector |= 1 << ((cols * rid) + (cid))
    # print('*' * 80)
    # print('iron man bit_vector', bit_vector)
    # print('iron man bin(bit_vector)', bin(bit_vector))
    return bit_vector


def find_min_flips(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    bit_vector = find_matrix_val(matrix)
    qu = deque()
    qu.append(bit_vector)
    steps = 0
    state_set = set()
    while qu:
        level_size = len(qu)
        for _ in range(level_size):
            bitv = qu.popleft()
            if not bitv:
                return steps

            for rid in range(rows):
                for cid in range(cols):
                    nex = bitv
                    for rx, cx in [(rid, cid), (rid - 1, cid), (rid, cid + 1),
                                   (rid + 1, cid), (rid, cid - 1)]:
                        if cols > cx >= 0 <= rx < rows:
                            nex ^= 1 << ((cols * rx) + cx)
                    if nex not in state_set:
                        state_set.add(nex)
                        qu.append(nex)
        steps += 1
    return -1
matrix = [[0, 0], [0, 1]]
# matrix = [[1, 0], [0, 1]]

print(find_min_flips(matrix))
