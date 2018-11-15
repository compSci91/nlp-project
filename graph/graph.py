import math

class GraphError(Exception):
    def GraphError(self, msg):
        super().__init__(msg)

class Vertex(object):
    '''
        A generic vertex of a graph.
    '''
    def __init__(self, prop):
        '''
            Vertex Constructor
            prop: Property of the vertex
        '''
        super().__init__()
        self.prop = prop
        self.adj_edges = set()

    def add_edge(self, adj):
        '''
            Adds an adjacent edge
            adj: the adjacent edge of this vertex
        '''
        if not adj.source == self and not adj.target == self:
            raise GraphError("Adding adjacent edge to vertex not on edge")

        if adj not in self.adj_edges:
            self.adj_edges.add(adj)

    def iter_edge(self):
        '''
            Iterate over the all edges
        '''
        for e in self.adj_edges:
            yield e


    def out_edges(self):
        '''
            Iterate over the out edges
        '''
        for e in self.adj_edges:
            if e.source == self:
                yield e

    def in_edges(self):
        '''
            Iterate over the in edges
        '''
        for e in self.adj_edges:
            if e.target == self:
                yield e

    def find_edge(self, target):
        '''
            Find an adjacent edge with specified target
            target: The target vertex of the edge
            return: The edge if found, or None if not.
        '''
        for e in self.out_edges():
            if e.target == target:
                return e
        return None


class Edge(object):
    '''
        A generic edge of a graph.
    '''
    def __init__(self, prop, source, target):
        '''
            Edge Constructor
            prop: The property of this edge
            source: the source vertex of this edge
            target: the target vertex of this edge
        '''
        super().__init__()
        self.prop = prop
        self.source = source
        self.target = target


class RelationGraph(object):
    '''
        Generic graph data structure for use in a NLP project
        Note: it only has the operators needed for this project.
    '''
    def __init__(self):
        '''
            Graph Constructor
        '''
        super().__init__()
        self.vertices = set()
        self.edges = set()

    def add_vertex(self, prop):
        '''
            Create an new vertex
            prop: The property of a new vertex
            return: The create vertex
        '''
        v = Vertex(prop)
        self.vertices.add(v)
        return v

    def add_edge(self, prop, source, target):
        '''
            Create a new edge
            prop: The property of this edge
            source: the source vertex of this edge
            target: the target vertex of this edge
            return: The created edge
        '''
        edge = Edge(prop, source, target)
        source.add_edge(edge)
        target.add_edge(edge)
        self.edges.add(edge)
        return edge

    def find_vertex(self, prop):
        '''
            Find a specific vertex with a give property
            prop: The property of this edge
            return: The vertex if found, None if not
        '''
        for v in self.vertices:
            if v.prop == prop:
                return v
        return None

    def find_edge(self, source, target):
        '''
            Find an edge
            source: the source vertex of this edge
            target: the target vertex of this edge
            return: An edge with source and target
        '''
        return source.find_edge(target)

    def iter_vertex(self):
        '''
            Iterate through all of the vertices
        '''
        for v in self.vertices:
            yield v

    def iter_edge(self):
        '''
            Iterate through all of the edges
        '''
        for e in self.edges:
            yield e

    def search(self, s, g):
        start = self.find_vertex(s)
        goal = self.find_vertex(g)
        weight = {}
        previous = {}
        for v in self.vertices:
            weight[v] = float("inf")
            previous[v] = v
        weight[start] = 0

        changed = True
        while changed:
            print("Inside while loop")
            changed = False
            for v in self.vertices:
                print("inside for loop")
                for e in v.in_edges():
                    #inefficient as it has to compute this everytime it
                    #looks at an edge and it looks at all the edges multiple
                    #times in a single query which will just increase with
                    #multiple queries
                    edgeWeight = math.log(e.prop) * -1
                    print("edge weight: {}".format(edgeWeight))
                    tempWeight = weight[e.source] + edgeWeight
                    if tempWeight < weight[v]:
                        weight[v] = tempWeight
                        previous[v] = e.source
                        changed = True

        path = []
        current = goal
        print("previous")
        for v,p in previous.items():
            print("{} to {}".format(p.prop,v.prop))
        while current != start:
            print(current)
            path.append(current)
            current = previous[current]
        path.append(start)
        path.reverse()

        return path
# Test case
if __name__ == '__main__':
    import random

    graph = RelationGraph()
    for x in range(0, 10):
        graph.add_vertex(x)

    for i in graph.iter_vertex():
        for j in graph.iter_vertex():
            if i == j:
      continue
            graph.add_edge(random.randint(1, 100)/100, i, j)

    for v in graph.iter_vertex():
        print(v.prop, end=" ")
        for e in v.iter_edge():
            print(e.prop, end=", ")
        print()

    path = graph.search(0,1)
    for v in path:
        print(v.prop)
