def total_time(start, graph):
    queue = []
    visited = set()
    queue.append(start)
    visited.add(start)
    total_time = 0

    while(queue):
        node_idx = queue.pop()
        node = graph[node_idx]
        total_time += node[0]
        print('*' * 80)
        print('iron man node', node)
        for nei in node[1]:

            if nei not in visited:
                queue.append(nei)
                visited.add(nei)
    return total_time


def calculate_time_taken():
    graph = {}
    # (time, [dependencies])
    graph[1] = (20, (2, 3))
    graph[2] = (10, (4,))
    graph[3] = (5, tuple())
    graph[4] = (5, tuple())
    return total_time(1, graph)


print(calculate_time_taken())
