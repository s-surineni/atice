# https://github.com/TheAlgorithms/Python/blob/master/data_structures/Graph/dijkstra_algorithm.py
import sys


class Graph:
    def __init__(self, num):
        self.adj_list = {}
        self.num_nodes = num
        self.dist_from_src = [sys.maxsize] * num
        self.parent = [-1] * num


    def dijkstra(self, src):
        self.parent = [-1] * self.num_nodes

        for vert in self.adj_list.keys():
            self.dist_from_src[vert] = sys.maxsize
            self.parent[vert] = -1

        self.dist_from_src[src] = 0
        p_q = PriorityQueue()
        p_q.insert(0, src)

        while not p_q.is_empty():
            current_v = p_q.extract_min()

            for vert, weight in self.adj_list[current_v]:
                new_dist = self.dist_from_src[current_v]
