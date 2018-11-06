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
from Article import Article

article = Article("Happy families are all alike; every unhappy family is unhappy in its own way.".lower())
article.printTest()
# def calculateNumberOfBigramsInCommon(firstBigrams, secondBigrams):
#     number_of_bigrams_in_common = 0
#     for bigram in firstBigrams:
#         if bigram in secondBigrams:
#             print bigram
#             number_of_bigrams_in_common += 1
#
#     return number_of_bigrams_in_common
#
# anna_karenina_constance_garnett = "Happy families are all alike; every unhappy family is unhappy in its own way.".lower()
#
# anna_karenina_constance_garnett_bigrams = set()
#
# bigrams = ngrams(anna_karenina_constance_garnett.split(), 2)
#
# for bigram in bigrams:
#     anna_karenina_constance_garnett_bigrams.add(bigram)
#
# # print anna_karenina_constance_garnett_bigrams
#
#
#
# #print "\n\n\n"
#
# anna_karenina_schwartz = "All happy families resemble one another; each unhappy family is unhappy in its own way.".lower()
#
# anna_karenina_schwartz_bigrams = set()
#
# bigrams = ngrams(anna_karenina_schwartz.split(), 2)
#
# for bigram in bigrams:
#     anna_karenina_schwartz_bigrams.add(bigram)
#
#
# print calculateNumberOfBigramsInCommon(anna_karenina_schwartz_bigrams, anna_karenina_constance_garnett_bigrams)
#print calculateNumberOfBigramsInCommon(anna_karenina_constance_garnett_bigrams, anna_karenina_schwartz_bigrams)
