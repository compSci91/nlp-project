from relations.article import Article
from graph.graph import RelationGraph
from utils.helpers import get_directory_files, get_article_names


class GramGraphGenerator:
    def __init__(self, corpus = 'mini_corpus'):
        articles_names = get_directory_files(corpus)
        print(articles_names)
        self.articles = [Article('./'+corpus+'/' + name) for name in articles_names]

        for article in self.articles:
            print(article.name)

    def build_graph(self, weight_calculator):
        graph = RelationGraph()
        vertex_map = {}

        #create vertices
        for article in self.articles:
            vertex_map[article.name] = graph.add_vertex(article.name)

        #build graph
        number_of_articles = len(self.articles)
        print(number_of_articles)
        for first_article_index in range(number_of_articles):
            for second_article_index in range(first_article_index+1, number_of_articles):
                # print("Firt Article Index " + str(first_article_index))
                # print("Second Article Index " + str(second_article_index))
                first_article = self.articles[first_article_index]
                second_article = self.articles[second_article_index]


                # weight = first_article.calculateNumberOfUnigramsInCommon(second_article)
                weight = weight_calculator.calculate_weight(first_article, second_article)
                # print("Weight between " + first_article.name + " and " + second_article.name + " is " + str(weight))

                first_vertex = vertex_map[first_article.name]
                second_vertex = vertex_map[second_article.name]

                if weight > 0.1:
                    print("Weight between " + first_article.name + " and " + second_article.name + " is " + str(weight))
                    graph.add_edge(weight, first_vertex, second_vertex)
                    graph.add_edge(weight, second_vertex, first_vertex)


        return graph
