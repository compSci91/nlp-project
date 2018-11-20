from nltk import ngrams
import re
import os

class Article:
    # there are static class variables.
    section_re = re.compile(r'^==\s*(?P<name>[\w -]+)\s*==$', re.MULTILINE)
    subsection_re = re.compile(r'^===\s*(?P<name>[\w -]+)\s*===$', re.MULTILINE)
    param_re = re.compile(r'[.!?]')

    class SubSection:
        def __init__(self, name, paras):
            self.name = name.strip()
            self.paras = paras

        def first_sentence(self):
            for x in self.paras:
                if len(x) == 0:
                    continue
                return x[0]
            return None

        def search(self, word):
            s = 0
            for p in self.paras:
                for sentence in p:
                    if word in sentence:
                        s += 1
            return s


    class Section:
        def __init__(self, name, subsections):
            self.name = name.strip()
            self.subsections = subsections

        def first_sentence(self):
            for x in self.subsections:
                if len(x.paras) == 0:
                    continue
                return x.first_sentence()
            return None

        def search(self, word):
            s = 0
            for x in self.subsections:
                s += x.search(word)
            return s


    def __init__(self, path, topic = None):
        self.contents = ""
        # print("Opening: ", path)
        with open(path) as file:
            self.contents = file.read().lower()
            self.name = os.path.basename(file.name)

        self.unigrams = set()
        self.bigrams = set()
        self.trigrams = set()
        self.topic = topic

        self.parags = []
        self.sects = []
        self.subsects= []
        self.sents = []
        self.built = False

        self.contentsUnigrams = ngrams(self.contents.split(), 1)
        self.contentsBigrams = ngrams(self.contents.split(), 2)
        self.contentsTrigrams = ngrams(self.contents.split(), 3)

        for unigram in self.contentsUnigrams:
            self.unigrams.add(unigram)

        for bigram in self.contentsBigrams:
            self.bigrams.add(bigram)

        for trigram in self.contentsTrigrams:
            self.trigrams.add(trigram)

    def get_section(self, name):
        for s in self.sections():
            if s.name == name:
                return s
        return None

    def build_groups(self):
        '''
            Sub divides the article into sections, subsections, paragraphs, and sentences
        '''
        self.built = True
        headers = self.section_names()
        sects = [x for x in Article.section_re.split(self.contents) if not x in headers]


        # for finding if this happens
        assert(len(headers) == len(sects))

        self.sects = []
        for (name, content) in zip(headers, sects):
            # this will return a list of subsect objects
            sec = self.sec_to_subsecs(name, content)
            self.subsects.extend(sec.subsections)
            self.sects.append(sec)

    def sec_to_subsecs(self, name, sec_text):
        '''
            Builds section from the section text
            name: section header name
            subsec: content of the section in a single string
            return: section object
        '''
        headers = self.subsection_names(sec_text)
        ssec = [x for x in Article.subsection_re.split(sec_text) if not x in headers]

        if len(headers) == len(ssec) - 1:
            headers = [''] + headers

        # same reason as line 68
        assert(len(headers) == len(ssec))

        subsects = []
        for (n, content) in zip(headers, ssec):
            ss = self.subsec_to_paragraph(n, content)
            subsects.append(ss)
            self.parags.extend(ss.paras)
        return self.Section(name, subsects)

    # builds the paragraphs from a subsections
    # a paragraph is a set of sentences
    def subsec_to_paragraph(self, name, subsec):
        '''
            Builds subsection from the subsection text
            name: sub section header name
            subsec: content of the sub section in a single string
            return: Subsection object
        '''
        param = subsec.split('\n')
        parags = []
        for p in param:
            sents = Article.param_re.split(p)
            pa = [x.strip() for x in sents if not len(x) == 0]
            if not len(pa) == 0:
                parags.append(pa)
                self.sents.extend(pa)
        return self.SubSection(name, parags)

    def section_names(self):
        '''
            Collects the names of all of the sections in an article
            returns: list of the section names
        '''
        # the first sections does have a title
        names = ['intro']
        for x in Article.section_re.finditer(self.contents):
            names.append(x.group('name'))
        return names

    def subsection_names(self, txt = None):
        '''
            Collects the names of subsections
            txt: the text to collect the subsections of.
            return: list of subsection names
            note: if txt is none (the default) then it will get all subsection names
        '''
        if txt is None:
            txt = self.contents

        names = []
        for x in Article.subsection_re.finditer(txt):
            names.append(x.group('name'))
        return names

    def sections(self):
        '''
            Returns the list of all sections in the article
            return: list of sections (see object)
        '''
        if not self.built:
            self.build_groups()

        return self.sects

    def subsections(self):
        '''
            Returns the list of all subsections in the article
            return: list of subsections (see object)
        '''
        if not self.built:
            self.build_groups()

        return self.subsects

    def paragraphs(self):
        '''
            Returns the list of all paragraphs in the article
            return: list of paragraphs (list of strings)
        '''
        if not self.built:
            self.build_groups()

        return self.parags

    def sentences(self):
        '''
            Returns the list of all sentences
            return: list of sentences (strings)
        '''
        if not self.built:
            self.build_groups()

        return self.sents

    def calculateNumberOfUnigramsInCommon(self, article):
        '''
            Calculates the number of unigrams in common with the given article
            article: The other Article, expected to be of type Article
            return: integer
        '''
        number_of_unigrams_in_common = 0
        for unigram in article.unigrams:
            if unigram in self.unigrams:
                # print bigram
                number_of_unigrams_in_common += 1

        return number_of_unigrams_in_common

    def calculateNumberOfBigramsInCommon(self, article):
        '''
            Calculates the number of bigrams in common with the given article
            article: The other Article, expected to be of type Article
            return: integer
        '''
        number_of_bigrams_in_common = 0
        for bigram in article.bigrams:
            if bigram in self.bigrams:
                # print bigram
                number_of_bigrams_in_common += 1

        return number_of_bigrams_in_common

    def calculateNumberOfTrigramsInCommon(self, article):
        '''
            Calculates the number of trigrams in common with the given article
            article: The other Article, expected to be of type Article
            return: integer
        '''
        number_of_trigrams_in_common = 0
        for trigram in article.trigrams:
            if trigram in self.trigrams:
                # print bigram
                number_of_trigrams_in_common += 1

        return number_of_trigrams_in_common

    def printTest(self):
        print(self.contents)
