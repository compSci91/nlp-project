# from relations.article import Article
from utils.helpers import get_article_names
from graph.graph import RelationGraph
import pprint


class Counts(object):
    def __init__(self):
        super().__init__()
        self.first_sentence = 0
        self.first_paragraph = 0
        self.total_count = 0
        self.sum = 0

    def compute_sum(self):
        self.sum = self.first_sentence + self.first_paragraph + self.total_count

    def __str__(self):
        return "{} {} {}".format(self.first_sentence, self.first_paragraph, self.total_count)

    def __format__(self, spec):
        return str(self)

    def __repr__(self):
        return str(self.__dict__)

class AtoA(object):
    FIRSTSENTENCE = 5
    FIRSTPARAGRAPH = 3
    TOTALCOUNT = 1

    BIAS = 0.1

    def __init__(self, topics, articles):
        super().__init__()
        z = zip(topics, articles)
        for (t, a) in z:
            a.topic = t
            # print(t)

        self.articles = {a.topic:a for a in articles}
        print(len(self.articles))
        self.data = {}
        self.ran = False

    def build_graph(self):
        if not self.ran:
            self.run()

# Create the graph
        g = RelationGraph()
        relation_sums = {}
#create a dictionary that maps the name of a vertex to the vertex object
        vertex_map = {}

# Building the sums, which will be used for the weights
        for v, c in self.data.items():
            if not v in relation_sums:
                relation_sums[v] = 0
            for _, i in c.items():
                relation_sums[v] += i.sum
        
# Building all the vertex
# for every vertex name, create a new vertex, store it in the map
        for a in self.articles.keys():
            vertex_map[a] = g.add_vertex(a)

#Building the edges
# graph.add_edge(for me, prop is the weight, and source and target are the vertex objects)
# This creates the edge uni-directionally
# Switch the source and target to add the other direction.
        for a, tb in self.data.items():
            # print("Looking at: {}".format(a))
            for b, c in tb.items():
                av = vertex_map[a]
                bv = vertex_map[b]
                # print("add_edge")
                weight = (c.sum) / (relation_sums[a] + AtoA.BIAS)
                weight_offset = self.data[b][a].sum / ((relation_sums[b] + AtoA.BIAS) * 2)

                if weight + weight_offset != 0:
                    g.add_edge(weight + weight_offset, av, bv)
        return g

    # I do not know what else to name this.
    def run(self):
        self.ran = True

        for ta, a in self.articles.items():
            for tb, b in self.articles.items():
                if ta == tb:
                    continue
                if not ta in self.data:
                    self.data[ta] = {}

                if not tb in self.data:
                    self.data[tb] = {}

                self.data[ta][tb] = Counts()
                self.data[tb][ta] = Counts()


        for ta, a in self.articles.items():
            for tb, b in self.articles.items():
                if ta == tb:
                    continue

                aintro = a.get_section('intro')
                bintro = b.get_section('intro')

                aintrocount = aintro.search(b.topic.lower()) * AtoA.FIRSTPARAGRAPH
                bintrocount = bintro.search(a.topic.lower()) * AtoA.FIRSTPARAGRAPH

                afirst = aintro.first_sentence()
                bfirst = bintro.first_sentence()

                afirstS = 0
                btopic = b.topic.lower()
                btopiclen = len(btopic)
                for aw in afirst.split():
                    if btopic == aw[0:btopiclen]:
                        afirstS += AtoA.FIRSTSENTENCE

                bfirstS = 0
                atopic = a.topic.lower()
                atopiclen = len(atopic)
                for bw in bfirst.split():
                    if atopic == bw[0:atopiclen]:
                        bfirstS += AtoA.FIRSTSENTENCE

                atotal = 0
                for s in a.sections():
                    atotal += s.search(b.topic.lower())

                btotal = 0
                for s in b.sections():
                    btotal += s.search(a.topic.lower())

                c = self.data[ta][tb]
                c.first_sentence = afirstS
                c.first_paragraph = afirstS + aintrocount
                c.total_count = atotal * AtoA.TOTALCOUNT

                c = self.data[tb][ta]
                c.first_sentence = bfirstS
                c.first_paragraph = bfirstS + bintrocount
                c.total_count = btotal * AtoA.TOTALCOUNT
                c.compute_sum()

        pprint.pprint(self.data)