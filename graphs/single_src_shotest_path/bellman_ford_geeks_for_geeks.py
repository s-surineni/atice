class Graph:
    def __init__(self, num_of_vertices):
        self.num_of_vertices = num_of_vertices
        self.edges = []     # holds the edges

    def add_edge(self, u, v, w):
        self.edges.append([u, v, w])

    def print_distances(self, dist):
        print('Vertex distance from source')
        for vertex in range(self.num_of_vertices):
            print('Vertex: {}, Dist: {}'.format(vertex, dist[vertex]))

    def bellman_ford(self, src):
        dist = [float('Inf')] * self.num_of_vertices

        dist[src] = 0

        for i in range(self.num_of_vertices):
            for u, v, w in self.edges:
                if dist[u] != float('Inf') and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
            print('')
            self.print_distances(dist)

        for u, v, w in self.edges:
            if dist[u] != float('Inf') and dist[u] + w < dist[v]:
                print('Graph contains negative weight cycle')
                return

g = Graph(5)
g.add_edge(0, 1, 1)
g.add_edge(0, 2, 4)
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 2)
g.add_edge(1, 4, 2)
g.add_edge(3, 2, 5)
g.add_edge(3, 1, 1)
g.add_edge(4, 3, 3)

#Print the solution
g.bellman_ford(0)

print('Total verices ', g.num_of_vertices)
