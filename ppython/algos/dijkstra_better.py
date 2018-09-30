# https://github.com/TheAlgorithms/Python/blob/master/data_structures/Graph/dijkstra_algorithm.py
import sys


class PriorityQueue():
    def __init__(self, size):
        self.curr_size = 0
        self.array= [None] * size
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
        if r_c < self.curr_size and self.array[r_c][0] < self.array[smallest][0]:
            smallest = r_c
        if smallest != idx:
            self.swap(idx, smallest)
            self.min_heapify(smallest)

    def swap(self, i, j):
        self.position[self.array[i][1]] = j
        self.position[self.array[j][1]] = i
        self.array[i], self.array[j] = self.array[j], self.array[i]

    def left_c_idx(self, idx):
        return (2 * idx) + 1

    def right_c_idx(self, idx):
        return (2 * idx) + 2

    def par_idx(self, idx):
        return idx // 2

    def decrease_key(self, d_v, new_dist):
        idx = self.position[d_v[1]]
        self.array[idx] = (new_dist, d_v[1])
        while idx > 0 and self.array[self.par_idx(idx)][0] > self.array[idx][0]:
            self.swap(idx, self.par_idx(idx))
            idx = self.par_idx(idx)

    def insert(self, d_v):
        self.position[d_v[1]] = self.curr_size
        print('*' * 80)
        print('curr_size', self.curr_size)
        print('array', self.array)
        self.array[self.curr_size] = (sys.maxsize, d_v[1])
        self.curr_size += 1
        # self.array.append((sys.maxsize, d_v[1]))
        self.decrease_key((sys.maxsize, d_v[1]), d_v[0])

    def extract_min(self):
        print('*' * 80)
        print('self.array', self.array)
        print('self.position', self.position)
        min_node = self.array[0][1]
        self.array[0] = self.array[self.curr_size - 1]
        self.curr_size -= 1
        self.min_heapify(0)
        print('min_node', min_node)
        del self.position[min_node]
        return min_node


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
        p_q = PriorityQueue(self.num_nodes)
        p_q.insert((0, src))

        while not p_q.is_empty():
            current_v = p_q.extract_min()

            for vert, weight in self.adj_list[current_v]:
                new_dist = self.dist_from_src[current_v] + weight

                if self.dist_from_src[vert] > new_dist:
                    if self.dist_from_src[vert] == sys.maxsize:
                        p_q.insert((new_dist, vert))
                    else:
                        p_q.decrease_key((self.dist_from_src[vert], vert), new_dist)
                    self.dist_from_src[vert] = new_dist
                    self.parent[vert] = current_v

        self.show_distances(src)

    def add_edge(self, start, end, weight):
        if start in self.adj_list.keys():
            self.adj_list[start].append((end, weight))
        else:
            self.adj_list[start] = [(end, weight)]

        if end in self.adj_list.keys():
            self.adj_list[end].append((start, weight))
        else:
            self.adj_list[end] = [(start, weight)]


    def show_distances(self, src):
        print('Distance from node: {}'.format(src))
        for vert in range(self.num_nodes):
            print('Node {} is at {} distance'.format(vert, self.dist_from_src[vert]))


if __name__ == '__main__':
    graph = Graph(9)
    graph.add_edge(0, 1, 4)
    graph.add_edge(0, 7, 8)
    graph.add_edge(1, 2, 8)
    graph.add_edge(1, 7, 11)
    graph.add_edge(2, 3, 7)
    graph.add_edge(2, 8, 2)
    graph.add_edge(2, 5, 4)
    graph.add_edge(3, 4, 9)
    graph.add_edge(3, 5, 14)
    graph.add_edge(4, 5, 10)
    graph.add_edge(5, 6, 2)
    graph.add_edge(6, 7, 1)
    graph.add_edge(6, 8, 6)
    graph.add_edge(7, 8, 7)
    # graph.show_graph()
    graph.dijkstra(0)
    # graph.show_path(0, 4)
