#!/usr/bin/env python
from nltk import ngrams

class Article:
    def __init__(self, path):
        file  = open(path, 'r')

        self.contents = file.read().lower()
        self.bigrams = set()

        self.contentsBigrams = ngrams(self.contents.split(), 2)

        for bigram in self.contentsBigrams:
            self.bigrams.add(bigram)

    def calculateNumberOfBigramsInCommon(self, article):
        number_of_bigrams_in_common = 0
        for bigram in article.bigrams:
            if bigram in self.bigrams:
                print bigram
                number_of_bigrams_in_common += 1

        return number_of_bigrams_in_common

    def printTest(self):
        print(self.contents)
