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

    def search(start, goal):
        weight = {}
        previous = {}
        startVertex = self.find_vertex(start)
        for v in self.vertices:
            weight[v] = float("inf")
            previous[v] = v
        weight[startVertex] = 0

        changed = True
        while changed:
            changed = False
            for v in self.vertices:
                if v == start
                for e in v.in_edges:
                    #inefficient as it has to compute this everytime it
                    #looks at an edge and it looks at all the edges multiple
                    #times in a single query which will just increase with
                    #multiple queries
                    edgeWeight = math.log(edge.prop) * -1
                    tempWeight = weight[e.source] + edgeWeight
                    if tempWeight < weight[v]:
                        weight[v] = tempWeight
                        previous[v] = e.source
                        changed = True

        path = []
        current = goal
        while current != start:
            path.append(current)
            current = previous[current]
        path.append[start]
        path.reverse()

        return path
