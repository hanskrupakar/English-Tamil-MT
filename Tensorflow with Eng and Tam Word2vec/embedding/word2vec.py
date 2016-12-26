# -*- coding: utf-8 -*-
from gensim.models import word2vec as wv
import numpy as np
import random
import re
import os

np.random.seed(10)

def return_english(c, n):

    if not os.path.exists("word2vec_%d.EN" % (n)):
        print("     creating Word2Vec vectors for English")
        with open("../dataset/src-train.txt", mode="r") as f:
            eng = f.read()
        if(eng[-1]!='\n'):
            eng += "\n"
        string=""
        for _ in xrange(500):
            string += "PAD "*np.random.randint(0, 2)
            string += "UNK "
            string += "PAD "*np.random.randint(0, 2)
            string += "UNK "
            string += "PAD "*np.random.randint(0, 3)
            string += "EOS "
            string += "GO"*np.random.randint(0, 2)
            string += "\n"
        eng += string
        
        sent=[]
        ewv=[]
        for e in unicode(eng, "utf-8").split("\n"):
            for p in e.strip().split(" "):
            	sent.append(p)
            ewv.append(filter(None, sent))
            sent=[]
        
        ewv=filter(None,ewv)

        modeleng = wv.Word2Vec(ewv, size=n, window=5, workers=4, batch_words=50, min_count=1)
        modeleng.save("word2vec_%d.EN" % (n))
        
        print("     Word2Vec model created and saved successfully!")
        
    modeleng = wv.Word2Vec.load("word2vec_%d.EN" % (n))
    vec = np.array([modeleng[x] for x in c])
    return vec


def create_tamil(n):

    print("     creating Word2Vec vectors for Tamil")
    with open("../dataset/clean.lm.tok.ta", mode="rb") as f:
        tam = f.read()
    with open("../dataset/targ-train.txt", mode="rb") as f:
        tam = f.read()
    if(tam[-1]!='\n'):
        tam += "\n"
    string=""
    for _ in xrange(500):
        string += "PAD "*np.random.randint(0, 2)
        string += "UNK "
        string += "PAD "*np.random.randint(0, 2)
        string += "UNK "
        string += "PAD "*np.random.randint(0, 3)
        string += "EOS "
        string += "GO"*np.random.randint(0, 2)
        string += "\n"
    tam += string
    
    sent=[]
    twv=[]
    for e in unicode(tam, "utf-8").split("\n"):
        for p in e.split(" "):
            sent.append(p)
        twv.append(filter(None, sent))
        sent=[]
    
    twv=filter(None,twv)
    
    modeltam = wv.Word2Vec(twv, size=n, window=5, workers=4, batch_words=50, min_count=1)
    modeltam.save("word2vec_%d.TA" % (n))
    
    print("     Word2Vec model created and saved successfully!")
    
def return_tamil(c, n):
        
    modeltam = wv.Word2Vec.load("word2vec_%d.TA" % (n))
    vec = np.array([modeltam[x] for x in c])
    return vec

def decode(x, n, vs):
    modeltam = wv.Word2Vec.load("word2vec_%d.TA" % (n))
    print(np.reshape(modeltam.similar_by_vector(x)[0], vs))

'''
Gensim Word2Vec Arguments: 

min count: threshold count for ignoring words
size: dimensionality of feature vectors
workers: parallelization (no of threads)
window: centre + window/2 elements on either side of the window
alpha: initial learning rate
max_vocab_size: threshold the vocabulary (prunes infrequent ones)
sample: probability threshold to downsample too frequent words (0 to 10^-5) [directly proportional to frequent words reduction]
sg: 0 - CBOW, 1 - Skip-Gram
hs: 1 - Hierarchical Softmax, 0 - Negative Sampling if negative==1
negative=n: n>0 - Negative Sampling (5 to 20 usually) no. of noise words, 0 - no Negative Sampling 
cbow_mean: if CBOW, 0: sum context word vectors, 1: mean context word vectors
hashfxn: hash function to use to randomly initialize weights, for increased training reproducibility
iter: no of iterations over the corpus.
trim_rule: vocabulary trimming rule, specifies whether certain words should remain in the vocabulary, be trimmed away, or handled using the default [applies iff word count > min_count]
sorted_vocab: if 1 (default), sort the vocabulary by descending frequency before assigning word indexes.
batch_words: target size (in words) for batches of examples passed to worker threads
'''
