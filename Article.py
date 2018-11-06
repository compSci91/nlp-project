#!/usr/bin/env python
from nltk import ngrams

class Article:
    def __init__(self, contents) :
        self.contents = contents
        self.bigrams = set()

        self.contentsBigrams = ngrams(self.contents.split(), 2)

        for bigram in self.contentsBigrams:
            self.bigrams.add(bigram)

    def calculateNumberOfBigramsInCommon(artcile):
        number_of_bigrams_in_common = 0
        for bigram in self.article.bigrams:
            if bigram in self.contentsBigrams:
                print bigram
                number_of_bigrams_in_common += 1

        return number_of_bigrams_in_common

    def printTest(self):
        print(self.contents)
