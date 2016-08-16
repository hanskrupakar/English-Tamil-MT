# -*- coding: utf-8 -*-
import io
import re
import numpy as np
from gensim.models import word2vec as wv

chars = [',',':','\'','\"','(',')','.']
with io.open('corpus.bcn.train.en','r',encoding='utf8') as f:
    eng = f.read()
eng=re.sub(u'(?u)[' + re.escape(''.join(chars)) + ']', '', eng)
modeleng = wv.Word2Vec(eng.split("\n"), size=100, window=5, workers=4, batch_words=50, sample=0.01, min_count=1)

with io.open('corpus.bcn.train.ta','r',encoding='utf8') as f:
    text = f.read()
text=re.sub(u'(?u)[' + re.escape(''.join(chars)) + ']', '', text)
pattern = re.compile(r"[ \n]")
tokens = list(set(pattern.split(text)))
temp=("அகமத்").decode('utf-8')

X=np.zeros((len(text.split("\n"))-1,30,100))
Y=np.zeros((len(text.split("\n"))-1,30,len(tokens)))
i=0
for sentence in text.split("\n"):
    if(sentence!=""):
        j=0
        l=sentence.split(" ")
        vec=[0] * len(tokens)
        for words in l:
            vec[tokens.index(words)]=1
            Y[i,j]=np.array(vec)
            j+=1
            vec=[0] * len(tokens)
    i+=1

i=0
for sentence in eng.split("\n"):
    if(sentence!=""):
        j=0
        l=sentence.split(" ")
        for words in l:
            print words
            '''X[i,j]=np.array(modeleng[words])'''
            j+=1
    i+=1

print X

'''
with io.open('corpus.bcn.train.en','r+',encoding='utf8') as f:
	text=f.read()
	text=text.replace(" <STOP> \n"," <STOP>\n")
	f.seek(0)
	f.truncate()
	f.write(text)
'''
