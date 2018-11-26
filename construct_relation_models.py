
from nltk import ngrams
# from Article import Article
from relations.article import Article
from relations.article_to_article import AtoA
from relations.topic_locality import TopicLocality
# from relations.topic_to_topic import TtoT
from utils.helpers import get_directory_files, get_article_names
from relations.gram_graph_generator import GramGraphGenerator
from relations.unigram_weight_calculator import UnigramWeightCalculator
from relations.bigram_weight_calculator import BigramWeightCalculator
from relations.trigram_weight_calculator import TrigramWeightCalculator

from graph.graph import RelationGraph
import sys



def construct_unigram_model(corpus):
    weight_calculator = UnigramWeightCalculator()
    graph = GramGraphGenerator(corpus.lower()).build_graph(weight_calculator)
    graph.save_graph(corpus.replace("_", "")+"Unigram.txt")

def construct_bigram_model(corpus):
    weight_calculator = BigramWeightCalculator()
    graph = GramGraphGenerator(corpus.lower()).build_graph(weight_calculator)
    graph.save_graph(corpus.replace("_", "")+"Bigram.txt")

def construct_trigram_model(corpus):
    weight_calculator = TrigramWeightCalculator()
    graph = GramGraphGenerator(corpus.lower()).build_graph(weight_calculator)
    graph.save_graph(corpus.replace("_", "")+"Trigram.txt")

def construct_AtoA_model(corpus):
    articles_names = get_directory_files('corpus')
    articles = [Article('./corpus/' + name) for name in articles_names]
    topics = get_article_names(articles_names)
    atoa = AtoA(topics, articles)
    atoa.run()
    graph = atoa.build_graph()
    graph.save_graph(corpus.replace("_", "")+"AtoA.txt")

def construct_topic_locality_model(corpus):
    articles_names = get_directory_files('corpus')
    articles = [Article('./corpus/' + name) for name in articles_names]
    topics = get_article_names(articles_names)
    locality = TopicLocality(topics,articles)
    directed = locality.buildDirectedGraph()
    directed.save_graph(corpus.replace("_", "")+"TopicLocalityDirected.txt")
    undirected = locality.buildUndirectedGraph()
    undirected.save_graph(corpus.replace("_", "")+"TopicLocalityUndirected.txt")

def main():
    corpus = 'Corpus'
    if 'mini' in sys.argv[1:]:
        corpus = 'Mini_Corpus'
        sys.argv.remove('mini')

    if len(sys.argv) < 2:
        construct_unigram_model(corpus)
        construct_bigram_model(corpus)
        construct_trigram_model(corpus)
        construct_AtoA_model(corpus)
        construct_topic_locality_model(corpus)
    elif 'u' in sys.argv[1:]:
        construct_unigram_model(corpus)
    elif 'b' in sys.argv[1:]:
        print(2)
        construct_bigram_model(corpus)
    elif 't' in sys.argv[1:]:
        construct_trigram_model(corpus)
    elif 'a' in sys.argv[1:]:
        construct_AtoA_model(corpus)
    elif 'l' in sys.argv[1:]:
        construct_topic_locality_model(corpus)
    elif len(sys.argv[1:]) >= 2:
        print("Please input '1' for unigram, '2' for bigram, '3' for trigram, 'AtoA' for Aricle to Article, 'L' for topic locality or nothing for all.")


if __name__ == '__main__':
    main()
