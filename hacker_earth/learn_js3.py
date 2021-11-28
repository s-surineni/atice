# how is it protected from paths where the path doesn't reach dest, how is it able to give correct value


def dfs(graph, start, end, visited, res):
    if start in visited:
        return res
    for idx in range(len(graph[start])):
        to = graph[start][idx][0]
        if to == end:
            res.append(start)
            print(start, end=" ")
            graph[start][idx][0] = "x"
            continue
        elif to == "x":
            continue
        res = dfs(graph, to, end, (visited | {start}), res)
    return res


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
    dfs(graph, start, end, set(), [])
    print()


print(learn_js())
