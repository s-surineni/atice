# https://github.com/TheAlgorithms/Python/blob/master/data_structures/Graph/dijkstra_algorithm.py
import sys


class PriorityQueue():
    def __init__(self):
        self.curr_size = 0
        self.array= []
        self.position = {}      # stores position of vertex in array

    def is_empty(self):
        return self.curr_size == 0

    def min_heapify(self, idx):
        l_c = self.left_c_idx(idx)
        r_c = self.right_c_idx(idx)

        if l_c < self.curr_size and self.array[l_c][0] < self.array[idx][0]:
            smallest = l_c
        else:
            smallest = idx
        if rc < self.self.curr_size and self.array[r_c][0] < self.array[smallest][0]:
            smallest = r_c
        if smallest != idx:
            self.swap(idx, smallest)
            self.min_heapify(smallest)

    def swap(self, i, j):
        self.pos[self.array[i][1]] = j
        self.pos[self.array[j][1]] = i
        self.array[i], self.array[j] = self.array[j], self.array[i]

    def left_c_idx(self, idx):
        return (2 * idx) + 1

    def right_c_idx(self, idx):
        return (2 * idx) + 2

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
                new_dist = self.dist_from_src[current_v] + weight

                if self.dist_from_src[vert] > new_dist:
                    if self.dist_from_src[vert] == sys.maxsize:
                        p_q.insert(new_dist, vert)
                    else:
                        p_q.decrease_key((self.dist_from_src[vert], vert), new_dist)
                    self.dist_from_src[vert] = new_dist
                    self.parent[vert] = current_v

        self.show_distances(src)


    def show_distances(self, src):
        print('Distance from node: {}'.format(src))
        for vert in range(self.num_nodes):
            print('Node {} is at {} distance'.format(vert, self.dist_from_src[vert]))
