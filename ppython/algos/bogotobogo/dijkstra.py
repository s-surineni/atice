import heapq
import sys


class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        self.distance = sys.maxsize
        self.visited = False
        self.previous = None

    def add_neighbor(self, neighor, weight=0):
        self.adjacent[neighor] = weight

    def get_connections(self):
        return self.adjacent.keys()

    def set_visited(self):
        self.visited = True

    def get_weight(self, neighor):
        return self.adjacent[neighor]


    def get_distance(self):
        return self.distance

    def set_distance(self, distance):
        self.distance = distance

    def set_previous(self, pre):
        self.previous = pre

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])


class Graph:
    def __init__(self):
        self.vertices = {}
        self.num_of_vertices = 0

    def __iter__(self):
        return iter(self.vertices.items())

    def add_vertex(self, node):
        self.num_of_vertices += 1
        new_vertex = Vertex(node)
        self.vertices[node] = new_vertex

    def get_vertex(self, vert):
        for a_vert in self.vertices:
            if a_vert == vert:
                return self.vertices[vert]

    def add_edge(self, frm, to, cost=0):
        if frm not in self.vertices:
            self.add_vertex(frm)
        if to not in self.vertices:
            self.add_vertex(to)

        self.vertices[frm].add_neighbor(self.vertices[to], cost)
        self.vertices[to].add_neighbor(self.vertices[frm], cost)


def dijkstra(a_graph, start, end):
    start.distance = 0

    unvisited_q = [(v.get_distance(), (k)) for (k, v) in a_graph]
    for u,v in unvisited_q:
        print(v)
    print(unvisited_q)
    heapq.heapify(unvisited_q)

    while len(unvisited_q):
        current_v = heapq.heappop(unvisited_q)
        current_v = a_graph.get_vertex(current_v[1])
        current_v.set_visited()
        # print('*' * 80)
        # print('current_v.adjacent', current_v.adjacent)
        for next in current_v.adjacent:
            if next.visited:
                continue
            new_dist = current_v.get_distance() + current_v.get_weight(next)
            if new_dist < next.get_distance():
                next.set_distance(new_dist)
                next.set_previous(current_v)


# if __name__ == '__main__':
# if True:
g = Graph()

g.add_vertex('a')
g.add_vertex('b')
g.add_vertex('c')
g.add_vertex('d')
g.add_vertex('e')
g.add_vertex('f')

g.add_edge('a', 'b', 7)  
g.add_edge('a', 'c', 9)
g.add_edge('a', 'f', 14)
g.add_edge('b', 'c', 10)
g.add_edge('b', 'd', 15)
g.add_edge('c', 'd', 11)
g.add_edge('c', 'f', 2)
g.add_edge('d', 'e', 6)
g.add_edge('e', 'f', 9)

dijkstra(g, g.get_vertex('a'), g.get_vertex('e'))
