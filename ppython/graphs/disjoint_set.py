from collections import defaultdict


class Graph:
    def __init__(self, num_of_v):
        self.num_of_v = num_of_v
        self.edges = defaultdict(list)

    def add_edge(self, v1, v2):
        self.edges[v1].append(v2)

    def find_parent(self, parent_list, ver):
        if parent_list[ver] == -1:
            return ver
        else:
            return self.find_parent(parent_list, parent_list[ver])

    def unite(self, parent_list, v1, v2):
        v1_rep = self.find_parent(parent_list, v1)
        v2_rep = self.find_parent(parent_list, v2)
        parent_list[v1_rep] = v2_rep

    def isGraphCyclic(self):
        parent_list = [-1] * self.num_of_v

        for v1 in self.edges:
            v1_rep = self.find_parent(parent_list, v1)
            for v2 in self.edges[v1]:
                v2_rep = self.find_parent(parent_list, v2)
                if v1_rep == v2_rep:
                    return True
                self.unite(parent_list, v1_rep, v2_rep)
        return False


g = Graph(3)
g.add_edge(0, 1)
g.add_edge(1, 2)
# g.add_edge(2, 0)
  
if g.isGraphCyclic():
    print("Graph contains cycle")
else:
    print("Graph does not contain cycle ")
