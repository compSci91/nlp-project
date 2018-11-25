from relations.article import Article

class BigramWeightCalculator:
    def calculate_weight(self, first_article, second_article):
        return first_article.calculateNumberOfBigramsInCommon(second_article)

    def getThreshold(self):
        return 0.02
