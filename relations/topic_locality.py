from relations.article import Article
from utils.helpers import get_article_names
from graph.graph import RelationGraph

import pprint

class TopicLocality(object):
    def __init__(self, topics, articles):
        super().__init__()
        self.topics = topics
        self.articles = articles

        self.primaryNodes = self.totalOccurrences()
    def run(self):
        pass
        
    def totalOccurrences(self):
        primaryNodes = {}
        for topicA in self.topics:
            secondaryNodes = {}
            for topicB in self.topics:
                if topicA == topicB:
                    continue
                articleCount = 0
                sectionCount = 0
                subsectionCount = 0
                paragraphCount = 0
                sentenceCount = 0
                for article in self.articles:
                    aInArt,bInArt = self.articleOccurence(article,topicA,topicB)
                    for section in article.sects:
                        aInSec,bInSec = self.sectionOccurrence(section,topicA,topicB)
                        for subsection in section.subsections:
                            aInSubsec,bInSubsec = self.subsectionOccurrence(subsection,topicA,topicB)
                            for paragraph in subsection.paras:
                                aInParag,bInParag = self.paragraphOccurrence(paragraph,topicA,topicB)
                                for sentence in paragraph:    								
                                    sentenceCount += self.sameSentenceOccurrence(sentence,topicA,topicB)
                                paragraphCount += aInParag * bInParag
                            subsectionCount += aInSubsec * bInSubsec
                        sectionCount += aInSec * bInSec
                    articleCount += aInArt * bInArt
                # print("OCURRENCES FOR: ",topicA,topicB, ", senteces: " , sentenceCount,", paragraphs: ", paragraphCount, ", subsections: ", subsectionCount, ", sections: ",sectionCount,", article: ",articleCount)
                total = sentenceCount * 1 + paragraphCount * 1 + subsectionCount * 1 + sectionCount * 1 + articleCount * 1
                secondaryNodes[topicB] = total
            primaryNodes[topicA] = secondaryNodes
        return primaryNodes 

    def buildUndirectedGraph(self):

        primaryNodes = self.primaryNodes

        denominator = 0
        vertex_map = {}
        g = RelationGraph()
        for a in primaryNodes.keys():
            vertex_map[a] = g.add_vertex(a)
            for b in primaryNodes[a].keys():
                denominator += primaryNodes[a][b]
        for a in primaryNodes.keys():
            for b in primaryNodes[a].keys():
                av = vertex_map[a]
                bv = vertex_map[b]
                if primaryNodes[a][b] != 0 :
                    g.add_edge((primaryNodes[a][b] / denominator), av, bv)
                    print("Adding edge: ",a, b,': ', (primaryNodes[a][b] / denominator))
        return g

    def buildDirectedGraph(self):
        primaryNodes = self.primaryNodes
        vertex_map = {}
        g = RelationGraph()
        for a in primaryNodes.keys():
            vertex_map[a] = g.add_vertex(a)
        for a in primaryNodes.keys():
            denominator = 0
            for b in primaryNodes[a].keys():
                denominator += primaryNodes[a][b]
            for b in primaryNodes[a].keys():
                av = vertex_map[a]
                bv = vertex_map[b]
                if primaryNodes[a][b] != 0 :
                    g.add_edge(((primaryNodes[a][b]+0.00001 )/ (denominator+1)), av, bv) #To avoid division by zero conflicts
                    print("Adding edge: ",a, b,': ', ((primaryNodes[a][b]+0.00001 )/ (denominator+1)))
        return g
               
    def sameSentenceOccurrence(self,sentence,topicA,topicB):
    	aInSent = 0
    	bInSent = 0 
    	for x in sentence.split():
    		if topicA in x:
    			aInSent += 1
    		if topicB in x:
    			bInSent += 1
    	return aInSent * bInSent 

    def sentenceOccurrence(self, sentence, topicA , topicB):
    	aInSent = 0
    	bInSent = 0
    	for x  in sentence.split():
    		if topicA in x:
    			aInSent += 1
    		if topicB in x:
    			bInSent += 1
    	return aInSent,bInSent

    def paragraphOccurrence(self,paragraph,topicA,topicB):
    	aInParag = 0
    	bInParag = 0
    	for sentence in paragraph:
    		aInSent,bInSent = self.sentenceOccurrence(sentence,topicA,topicB)
    		aInParag += aInSent
    		bInParag += bInSent
    	return aInParag,bInParag

    def subsectionOccurrence(self,subsection,topicA,topicB):
    	aInSubsec = 0
    	bInSubsec = 0
    	for paragraph in subsection.paras:
    		aInParag,bInParag = self.paragraphOccurrence(paragraph,topicA,topicB)
    		aInSubsec += aInParag
    		bInSubsec += bInParag
    	return aInSubsec,bInSubsec

    def sectionOccurrence(self,section,topicA,topicB):
    	aInSec = 0
    	bInSec = 0
    	for subsection in section.subsections:
    		aInSubsec,bInSubsec = self.subsectionOccurrence(subsection,topicA,topicB)
    		aInSec += aInSubsec
    		bInSec += bInSubsec
    	return aInSec,bInSec

    def articleOccurence(self,article,topicA,topicB):
    	aInArt = 0
    	bInArt = 0
    	for section in article.sects:
    		aInSec,bInSec = self.sectionOccurrence(section,topicA,topicB)
    		aInArt += aInSec
    		bInArt += bInSec
    	return aInArt,bInArt			

	