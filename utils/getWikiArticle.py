import sys
from wikipedia import Wikipedia
from wiki2plain import Wiki2Plain

lang = 'en'
wiki = Wikipedia(lang)

try:
    articleName = str(sys.argv[1])#'Uruguay'
    raw = wiki.article(articleName)
except:
    raw = None

if raw:
    wiki2plain = Wiki2Plain(raw)
    f = open('./corpus/' + articleName + '.txt', 'w')
    f.write(wiki2plain.text)
    #content = wiki2plain.text
    #print(wiki2plain.text)
