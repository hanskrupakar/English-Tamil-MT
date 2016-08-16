import random
from gensim.models import word2vec as wv
from tensorflow.python.platform import gfile
import re
import numpy as np

_WORD_SPLIT = re.compile(b"([.,!?$%\"':;)(])")

if not gfile.Exists("Dataset/word2vec_vocab%d.TA" % 4000):
    print(" creating Word2Vec vectors for Tamil")
    with gfile.GFile("Dataset/TAMIL_TRAIN", mode="rb") as f:
        tam = f.read()
    if(tam[-1]!='\n'):
        tam += "\n"
    string=""
    for _ in xrange(500):
        string += "_PAD "*np.random.randint(0, 2)
        string += "_UNK "
        string += "_PAD "*np.random.randint(0, 2)
        string += "_UNK "
        string += "_PAD "*np.random.randint(0, 3)
        string += "_EOS "
        string += "_GO"*np.random.randint(0, 2)
        string += "\n"
    tam += string
    
    sent=[]
    twv=[]
    for e in unicode(tam, "utf-8").split("\n"):
        for p in e.split(" "):
            sent.extend(re.split(_WORD_SPLIT, p))
        twv.append(filter(None, sent))
        sent=[]
    
    twv=filter(None,twv)
    
    modeleng = wv.Word2Vec(twv, size=50, window=5, workers=4, batch_words=50, min_count=1)
    modeleng.save("Dataset/word2vec_vocab%d.TA" % 4000)
    
    print(" Word2Vec model created and saved successfully!")