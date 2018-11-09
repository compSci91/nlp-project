#!/usr/bin/env python
from nltk import ngrams

class Article:
    def __init__(self, path):
        file  = open(path, 'r')

        self.contents = file.read().lower()
        self.unigrams = set()
        self.bigrams = set()
        self.trigrams = set()

        self.contentsUnigrams = ngrams(self.contents.split(), 1)
        self.contentsBigrams = ngrams(self.contents.split(), 2)
        self.contentsTrigrams = ngrams(self.contents.split(), 3)

        for unigram in self.contentsUnigrams:
            self.unigrams.add(unigram)

        for bigram in self.contentsBigrams:
            self.bigrams.add(bigram)

        for trigram in self.contentsTrigrams:
            self.trigrams.add(trigram)

    def calculateNumberOfUnigramsInCommon(self, article):
        number_of_unigrams_in_common = 0
        for unigram in article.unigrams:
            if unigram in self.unigrams:
                # print bigram
                number_of_unigrams_in_common += 1

        return number_of_unigrams_in_common

    def calculateNumberOfBigramsInCommon(self, article):
        number_of_bigrams_in_common = 0
        for bigram in article.bigrams:
            if bigram in self.bigrams:
                # print bigram
                number_of_bigrams_in_common += 1

        return number_of_bigrams_in_common

    def calculateNumberOfTrigramsInCommon(self, article):
        number_of_trigrams_in_common = 0
        for trigram in article.trigrams:
            if trigram in self.trigrams:
                # print bigram
                number_of_trigrams_in_common += 1

        return number_of_trigrams_in_common

    def printTest(self):
        print(self.contents)
