from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)


    def addEdge(self, u, v):
        self.graph[u].append(v)


    def bfs(self, s):
        visited = [False] * len(self.graph)

        queue = [s]

        while queue:
            u = queue.pop(0)
            print('adjacent to %s' % u)
            for v in self.graph[u]:
                # print('v, ', v)
                if not visited[v]:
                    visited[v] = True
                    print(v)
                    queue.append(v)


if __name__ == '__main__':
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 3)
    g.addEdge(1, 2)
    g.addEdge(2, 1)
    g.addEdge(3, 4)
    g.addEdge(3, 5)
    g.addEdge(4, 5)
    g.addEdge(4, 7)
    g.addEdge(5, 6)
    g.addEdge(5, 7)
    g.addEdge(6, 7)
    g.addEdge(7, 6)

    g.bfs(0)
