# file  = open('./corpus/Agriculture.txt', 'r')
#
# for line in file:
#     print(line)
#
# file.close


# def printSomeStuff():
#     print "Hello, methods!"
#
# printSomeStuff()

from nltk import ngrams
# from Article import Article
from relations.article import Article
from relations.article_to_article import AtoA
from relations.topic_locality import TopicLocality

from utils.helpers import get_directory_files, get_article_names
from relations.gram_graph_generator import GramGraphGenerator
from relations.unigram_weight_calculator import UnigramWeightCalculator
from relations.bigram_weight_calculator import BigramWeightCalculator
from relations.trigram_weight_calculator import TrigramWeightCalculator

from graph.graph import RelationGraph

# There is an error decoding the text files

# articles_names = get_directory_files('corpus')
# articles = [Article('./corpus/' + name) for name in articles_names]
# topics = get_article_names(articles_names)
# atoa = TtoT(topics, articles)
# atoa.run()
articles_names = get_directory_files('corpus')
articles = [Article('./corpus/' + name) for name in articles_names]
topics = get_article_names(articles_names)

# atoa = AtoA(topics, articles)
# atoa.run()
# graph = atoa.build_graph()
# # print(len(graph.vertices))
# # print(len(graph.edges))

weight_calculator = UnigramWeightCalculator()
graph = GramGraphGenerator().build_graph(weight_calculator)
graph.save_graph("MiniCorpusUnigram.txt")

for vertex in graph.iter_vertex():
    print(vertex.prop)
    for edge in vertex.iter_edge():
        print(edge.source.prop, end=" ")
        print(" == ", end=" ")
        print(edge.prop, end=" ")
        print(" ==>", end=" ")
        print(edge.target.prop)
    print()
# path = graph.search('agriculture', 'plants')
# print(path)

tl = TopicLocality(topics, articles)
g = tl.buildUndirectedGraph()

graph2 = RelationGraph()
graph2.load_graph('RelationModels/MiniCorpusUnigram.txt')
print("number of vertices %f" % len(graph2.vertices))
for vertex in graph2.iter_vertex():
    print(vertex.prop)
    for edge in vertex.iter_edge():
        print(edge.source.prop, end=" ")
        print(" == ", end=" ")
        print(edge.prop, end=" ")
        print(" ==>", end=" ")
        print(edge.target.prop)
    print()

# print("Number of unigrams in common ", bovine.calculateNumberOfUnigramsInCommon(cattle))
# print("Number of bigrams in common: ", bovine.calculateNumberOfBigramsInCommon(cattle))
# print("Number of trigrams in common: ", bovine.calculateNumberOfTrigramsInCommon(cattle))
