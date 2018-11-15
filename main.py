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
from utils.helpers import get_directory_files, get_article_names

bovine = Article('./corpus/Bovine.txt')
cattle = Article("./corpus/cattle.txt")

# There is an error decoding the text files

# articles_names = get_directory_files('corpus')[0:10]
# articles = [Article('./corpus/' + name) for name in articles_names]
# topics = get_article_names(articles)
# atoa = AtoA(topics, articles)

print("Number of unigrams in common ", bovine.calculateNumberOfUnigramsInCommon(cattle))
print("Number of bigrams in common: ", bovine.calculateNumberOfBigramsInCommon(cattle))
print("Number of trigrams in common: ", bovine.calculateNumberOfTrigramsInCommon(cattle))
