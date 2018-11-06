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

bovine = Article("./corpus/Bovine.txt")
cattle = Article("./corpus/cattle.txt")

print "Number of unigrams in common ", bovine.calculateNumberOfUnigramsInCommon(cattle)
print "Number of bigrams in common: ", bovine.calculateNumberOfBigramsInCommon(cattle)
print "Number of trigrams in common: ", bovine.calculateNumberOfTrigramsInCommon(cattle)
