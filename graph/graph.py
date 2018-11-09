class Vertex(object):
    def __init__(self, prop):
        super().__init__()
        self.prop = prop
        self.adj_edges = set()

    def add_edge(self, adj):
        if adj not in self.adj_edges:
            self.adj_edges.add(adj)

    def out_edges(self):
        for e in self.adj_edges:
            if e.source == self:
                yield e

    def in_edges(self):
        for e in self.adj_edges:
            if e.target == self:
                yield e

    def find_edge(self, target):
        for e in self.adj_edges:
            if e.target == target:
                return e
        return None


class Edge(object):
    def __init__(self, prop, source, target):
        super().__init__()
        self.prop = prop
        self.source = source
        self.target = target


class RelationGraph(object):
    def __init__(self):
        super().__init__()
        self.vertices = set()
        self.edges = set()

    def add_vertex(self, prop):
        v = Vertex(prop)
        self.vertices.add(v)
        return v

    def add_edge(self, prop, source, target):
        edge = Edge(prop, source, target)
        source.add_edge(edge)
        target.add_edge(edge)
        self.edges.add(edge)
        return edge

    def find_vertex(self, prop):
        for v in self.vertices:
            if v.prop == prop:
                return v
        return None

    def find_edge(self, source, target):
            return source.find_edge(target)
