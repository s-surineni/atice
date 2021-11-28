def dfs(graph, start, end, visited, res):
    if start in visited:
        return res
    for idx in range(len(graph[start])):
        to = graph[start][idx][0]
        if to == end:
            return 1
        dfs(graph, to, end, (visited | {start}), res)
    return 0


def learn_js():
    vertices = int(input())
    graph = {}
    for _ in range(vertices):
        vertex = int(input().strip())
        graph[vertex] = []
    total_edges = int(input().strip())
    for _ in range(total_edges):
        st, to = [int(i) for i in input().strip().split()]
        graph[st].append([to])
    start = int(input().strip())
    end = int(input().strip())
    return dfs(graph, start, end, set(), [])


print(learn_js())
