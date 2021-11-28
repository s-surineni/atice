# how is it protected from paths where the path doesn't reach dest, how is it able to give correct value
import math


def dfs(graph, start, end, visited, dist, res):
    if start in visited:
        return res
    if start == end and res > dist:
        return dist
    for to, weight in graph[start]:
        res = dfs(graph, to, end, (visited | {start}), dist + weight, res)
    return res


def learn_js():
    vertices = int(input())
    graph = {}
    for _ in range(vertices):
        vertex = int(input().strip())
        graph[vertex] = []
    total_edges = int(input().strip())
    for _ in range(total_edges):
        st, to, weight = [int(i) for i in input().strip().split()]
        graph[st].append((to, weight))
    start = int(input().strip())
    end = int(input().strip())
    return dfs(graph, start, end, set(), 0, math.inf)


print(learn_js())
