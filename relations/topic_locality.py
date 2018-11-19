from relations.article import Article
from utils.helpers import get_article_names

class TopicLocality(object):
    def __init__(self, topics, articles):
        super().__init__()
        self.topics = topics
        self.articles = articles

    def run(self):
        pass

    def totalOccurrences(self):
    	for topicA in self.topics:
    		for topicB in self.topics:
    			if topicA == topicB:
    				continue
    			articleCount = 0
    			sectionCount = 0
    			subsectionCount = 0
    			paragraphCount = 0
    			sentenceCount = 0
    			for article in self.articles:
    				article.build_groups()
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
    			print("OCURRENCES FOR: ",topicA,topicB, "\nsenteces: " , sentenceCount,"\nparagraphs: ", paragraphCount, "\nsubsections: ", subsectionCount, "\nsections: ",sectionCount,"\narticle: ",articleCount)

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

	