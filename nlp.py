import nltk
#nltk.download()
import re
from nltk.tokenize import RegexpTokenizer





path='page*txt'

tokenAll=[]
for j in glob.glob(path):
    f=open(j,'r')
    raw=f.read()
    #tokenizer = nltk.data.load('nltk:tokenizers/punkt/english.pickle')
    tokenizer = RegexpTokenizer(r'\w+')
    raw = raw.decode('utf8')
    tokens=tokenizer.tokenize(raw)
    #tokens = nltk.word_tokenize(raw)
    tokenAll.extend(tokens)

for word in tokenAll:
    word = word.lower()
    if word.isalpha(): # drop all non-words
        clean_tokens.append(word)
    
text = nltk.Text(clean_tokens)
text.dispersion_plot(['shock','stress','shortage','water','energy','taxes','people'])




stopwords = nltk.corpus.stopwords.words('english')
allWordExceptStopDist = nltk.FreqDist(w.lower() for w in text if w not in stopwords)  
allWordExceptStopDist.plot(30,cumulative=True)


text.dispersion_plot(['shock','stress','shortage','water','energy','taxes','people'])
#neutral: 0.8
#polar: 0.2

#
#fd = nltk.FreqDist(text) #–fd[‘the’] – how many occurences of the word ‘the’
##fd.keys() – show the keys in the data object
#fd.values() – show the values in the data object
#fd.items() – show everything
#fd.keys()[0:50] – just show a portion of the info.
#fd.plot(50,cumulative=False) – generate a chart of the 50 most frequent words