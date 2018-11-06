# file  = open('./corpus/Agriculture.txt', 'r')
#
# for line in file:
#     print(line)
#
# file.close

from nltk import ngrams

anna_karenina_constance_garnett = "Happy families are all alike; every unhappy family is unhappy in its own way.".lower()

anna_karenina_constance_garnett_bigrams = set()

bigrams = ngrams(anna_karenina_constance_garnett.split(), 2)

for bigram in bigrams:
    anna_karenina_constance_garnett_bigrams.add(bigram)

#print anna_karenina_constance_garnett_bigrams



#print "\n\n\n"

anna_karenina_schwartz = "All happy families resemble one another; each unhappy family is unhappy in its own way.".lower()

anna_karenina_schwartz_bigrams = set()

bigrams = ngrams(anna_karenina_schwartz.split(), 2)

for bigram in bigrams:
    anna_karenina_schwartz_bigrams.add(bigram)

#print anna_karenina_schwartz_bigrams

number_of_bigrams_in_common = 0

for anna_karenina_constance_garnett_bigram in anna_karenina_constance_garnett_bigrams:
    if anna_karenina_constance_garnett_bigram in anna_karenina_schwartz_bigrams:
        number_of_bigrams_in_common += 1
        print anna_karenina_constance_garnett_bigram

print "Number of bigrams in common ", number_of_bigrams_in_common
