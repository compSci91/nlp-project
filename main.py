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

constance_garnett = Article("Happy families are all alike; every unhappy family is unhappy in its own way.".lower())
# constance_garnett.printTest()

schwartz = Article("All happy families resemble one another; each unhappy family is unhappy in its own way.".lower())

print constance_garnett.calculateNumberOfBigramsInCommon(schwartz)
