import sys
from dijkstra_better import PriorityQueue


class Graph:
    def __init__(self, vert_num):
        self.adj_list = {}
        self.num_nodes = vert_num

    def prim_mst(self):
        self.vert_parent = [-1] * self.num_nodes
        self.dist_from_src = [sys.maxsize] * self.num_nodes

        # we can select any vertex but I am selecting 0
        self.dist_from_src[0] = 0
        p_q = PriorityQueue(self.num_nodes)
        p_q.insert((0, 0))

        while not p_q.is_empty():
            current_v = p_q.extract_min()

            for vert, weigh in self.adj_list[current_v]:
                new_dist = self.dist_from_src[current_v] + weigh
                if self.dist_from_src[vert] > new_dist:
                    if self.dist_from_src[vert] == sys.maxsize:
                        p_q.insert((new_dist, vert))
                    else:
                        p_q.decrease_key((self.dist_from_src[vert], vert), new_dist)
                    self.dist_from_src[vert] = new_dist
                    self.vert_parent[vert] = current_v
        return self.vert_parent


    def add_edge(self, start, end, weight):
        if start in self.adj_list.keys():
            self.adj_list[start].append((end, weight))
        else:
            self.adj_list[start] = [(end, weight)]

        if end in self.adj_list.keys():
            self.adj_list[end].append((start, weight))
        else:
            self.adj_list[end] = [(start, weight)]


if __name__ == '__main__':
    g = Graph(4)
    g.add_edge(0, 1, 100)
    g.add_edge(0, 2, 6)
    g.add_edge(0, 3, 5)
    g.add_edge(1, 3, 15)
    g.add_edge(2, 3, 4)

    print(g.prim_mst())
