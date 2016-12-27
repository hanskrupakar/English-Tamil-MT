# -*- coding: utf-8 -*-
from keras.models import Sequential
from keras.layers.core import Activation, TimeDistributedDense, RepeatVector
from keras.layers import recurrent
import io
from gensim.models import word2vec as wv
import re
from keras.models import model_from_json
import numpy as np


def decode(p):
    return np.where(p==np.amax(p))[0][0]

chars = [',',':','\"','(',')','.']
with io.open('corpus.bcn.train.ta','r',encoding='utf8') as f:
    text = f.read()
text=re.sub(u'(?u)[' + re.escape(''.join(chars)) + ']', '', text)
text=text.replace("\n"," <STOP>\n")
pattern = re.compile(r"[ \n]")
tokens = list(set(pattern.split(text)))

with open('corpus.bcn.train.en','r') as f:
    eng = f.read()
eng=eng.replace("\n"," <STOP>\n")
eng=re.sub(u'(?u)[' + re.escape(''.join(chars)) + ']', '', eng)
ewv=[e.split(" ") for e in eng.split("\n")]
ewv.pop(20)
modeleng = wv.Word2Vec(ewv, size=100, window=5, workers=4, batch_words=50, min_count=1)

model=Sequential()
model = model_from_json(open('my_model_architecture.json').read())
model.load_weights('my_model_weights.h5')

X_val=np.zeros((1,50,100))
Y_val=np.zeros((1,30,len(tokens)))
outta=[x for x in "தனது மனைவி மகளுடன் அஞ்சாதே படத்தை ரசித்தார் விஜய் <STOP>".decode('utf-8').split(" ")]
i=0
for i in xrange(len(outta)):
    Y_val[0,i,tokens.index(outta[i])]=1
outen="Julius Rosenberg accompanied with his wife and daughter enjoyed the film Anjathey <STOP>".split(" ")
i=0
for words in outen:
    X_val[0,i]=np.array(modeleng[words])
    i+=1

preds = model.predict(X_val, verbose=0)
predop=""
print tokens[12]
for i in range(30):
        predop=predop+" "+tokens[decode(preds[0,i])]
predop=predop[:predop.index(unicode("<STOP>"))]
print("ENG: Vijay accompanied with his wife and daughter enjoyed the film Anjathey <STOP>")
print("TAMIL:  தனது மனைவி மகளுடன் அஞ்சாதே படத்தை ரசித்தார் விஜய் <STOP>")
print("PREDICTED: "+predop)
print('---')
