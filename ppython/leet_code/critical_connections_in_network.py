from collections import defaultdict


def find_critical_connections(edges, connects):
    def make_graph(connects):
        graph = defaultdict(list)
        for to, fro in connects:
            graph[to].append(fro)
            graph[fro].append(to)
        return graph

    graph = make_graph(connects)
    connects = set(map(tuple, map(sorted, connects)))
    print(connects)
    node_depth = [None] * edges

    def dfs(node, depth):
        if node_depth[node] is not None:
            return node_depth[node]
        node_depth[node] = depth
        min_depth = edges
        for an in graph[node]:
            if node_depth[an] == depth - 1:
                continue
            curr_depth = dfs(an, depth + 1)
            if curr_depth <= depth:
                connects.discard((node, an) if node < an else (an, node))
            min_depth = min(curr_depth, min_depth)
        return min_depth
    dfs(0, 0)
    return len(connects)

n = 4
connections = [[0, 1], [1, 2], [2, 0], [1, 3]]
print(find_critical_connections(n, connections))
