def find_num_of_vertices(count, edges):
    vert_in = [0] * count
    for out, inn in edges:
        vert_in[inn] += 1
    resp = []
    for idx, vr in enumerate(vert_in):
        if not vr:
            resp.append(idx)
    return resp


n = 5
edges = [[0, 1], [2, 1], [3, 1], [1, 4], [2, 4]]
print(find_num_of_vertices(n, edges))