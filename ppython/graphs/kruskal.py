from collections import defaultdict


class Graph:
    def __init__(self, num_of_v):
        self.num_of_v = num_of_v
        self.edges = []

    def add_edge(self, u, v, w):
        self.edges.append((u, v, w))

    def find(self, subsets, v):
        if subsets[v][0] == v:
            return v
        else:
            return self.find(subsets, subsets[v][0])

    def union(self, subsets, u_rep, v_rep):
        if subsets[u_rep][1] > subsets[v_rep][1]:
            subsets[v_rep][0] = u_rep
        elif subsets[v_rep][1] > subsets[u_rep][1]:
            subsets[u_rep][0] = v_rep
        else:
            subsets[v_rep][0] = u_rep
            subsets[u_rep][1] += 1

    def kruskal_mst(self):
        result = []
        self.edges.sort(key=lambda edge: edge[2])

        subsets = []
        # key stores vertex value is its rank
        for node in range(self.num_of_v):
            subsets.append([node, 0])

        for edge in range(self.num_of_v):
            u, v, w = self.edges[edge]
            u_rep = self.find(subsets, u)
            v_rep = self.find(subsets, v)

            if u_rep != v_rep:
                result.append((u, v, w))
                self.union(subsets, u_rep, v_rep)
        return result


g = Graph(4)

g = Graph(4)
g.add_edge(0, 1, 10)
g.add_edge(0, 2, 6)
g.add_edge(0, 3, 5)
g.add_edge(1, 3, 15)
g.add_edge(2, 3, 4)

print(g.kruskal_mst())
