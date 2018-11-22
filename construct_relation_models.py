
from nltk import ngrams
# from Article import Article
from relations.article import Article
from relations.article_to_article import AtoA
# from relations.topic_to_topic import TtoT
from utils.helpers import get_directory_files, get_article_names
from relations.gram_graph_generator import GramGraphGenerator
from relations.unigram_weight_calculator import UnigramWeightCalculator
from relations.bigram_weight_calculator import BigramWeightCalculator
from relations.trigram_weight_calculator import TrigramWeightCalculator

from graph.graph import RelationGraph
import sys

def construct_unigram_model():
    weight_calculator = UnigramWeightCalculator()
    graph = GramGraphGenerator('corpus').build_graph(weight_calculator)
    graph.save_graph("CorpusUnigram.txt")

def construct_bigram_model():
    weight_calculator = BigramWeightCalculator()
    graph = GramGraphGenerator('corpus').build_graph(weight_calculator)
    graph.save_graph("CorpusBigram.txt")

def construct_trigram_model():
    weight_calculator = TrigramWeightCalculator()
    graph = GramGraphGenerator('corpus').build_graph(weight_calculator)
    graph.save_graph("CorpusTrigram.txt")

def construct_AtoA_model():
    print('AtoA')

def construct_topic_locality_model():
    print('Topic Locality')

def main():
    if len(sys.argv) < 2:
        construct_unigram_model()
        construct_bigram_model()
        construct_trigram_model()
        construct_AtoA_model()
        construct_topic_locality_model()
    elif '1' in sys.argv[1:]:
        construct_unigram_model()
    elif '2' in sys.argv[1:]:
        print(2)
        construct_bigram_model()
    elif '3' in sys.argv[1:]:
        construct_trigram_model()
    elif 'AtoA' in sys.argv[1:]:
        construct_AtoA_model()
    elif 'L' in sys.argv[1:]:
        construct_topic_locality_model()
    elif len(sys.argv[1:]) >= 2:
        print("Please input '1' for unigram, '2' for bigram, '3' for trigram, 'AtoA' for Aricle to Article, 'L' for topic locality or nothing for all.")


if __name__ == '__main__':
    main()
