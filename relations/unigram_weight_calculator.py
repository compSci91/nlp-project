from relations.article import Article

class UnigramWeightCalculator:
    def calculate_weight(self, first_article, second_article):
        return first_article.calculateNumberOfUnigramsInCommon(second_article)
