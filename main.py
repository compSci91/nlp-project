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

print bovine.calculateNumberOfBigramsInCommon(cattle)
