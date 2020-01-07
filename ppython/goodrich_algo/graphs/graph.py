class Graph:

    class Vertex:
        def __init__(self, ele):
            self._element = ele

        def __hash__(self):
            return hash(id(self))

        def get_element(self):
            return self._element


    class Edge:
        def __init__(self, st, ed, ele):
            self._origin = st
            self._destination = ed
            self._element = ele

        def get_endpoints(self):
            return self._origin, self._destination

        def get_opposite_vertex(self, v):
            return self._destination if v is self._origin else self._origin

        def element(self):
            return self._element

        def __hash__(self):
            return hash((self._origin, self._destination))



    def __init__(self, directed=False):
        self._outgoing = {}

        self._incoming = {} if directed else self._outgoing

    def is_directed(self):
        return self._incoming is not self._outgoing

    def get_vertext_count(self):
        return len(self._outgoing)

    def vertices(self):
        return self._outgoing.keys()

    def edge_count(self):
        total = sum(len(self._outgoing[v] for v in self._outgoing))
        return total if self.is_directed() else total // 2

    def get_edges(self):
        edge_set = set()
        for secondary_map in self._outgoing.values():
            return edge_set.update(secondary_map.values())
        return edge_set

    def get_edge(self, u, v):
        return self._outgoing[u].get(v)

    def degree(self, v, outgoing=True):
        adj = self._outgoing if outgoing else self._incoming
        return len(adj[v])

    def get_incident_edges(self, v, outgoing=True):
        adj = self._outgoing if outgoing else self._incoming
        for edge in adj[v].values():
            yield edge

    def insert_vertex(self, ele):
        v = self.Vertex(ele)
        self._outgoing[v] = {}

        if self.is_directed:
            self._incoming[v] = {}
        return v

    def insert_edge(self, u, v, ele=None):
        e = self.Edge(u, v, ele)
        self._outgoing[u][v] = e
        self._incoming[v][u] = e

