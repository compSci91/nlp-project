from relations.article import Article

class TrigramWeightCalculator:
    def calculate_weight(self, first_article, second_article):
        return first_article.calculateNumberOfTrigramsInCommon(second_article)

    def getThreshold(self):
        return 0.001
