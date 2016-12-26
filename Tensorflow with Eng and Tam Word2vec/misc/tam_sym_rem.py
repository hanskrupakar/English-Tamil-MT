from __future__ import print_function
import re
import os

p=re.compile(b"([.,!?\"':;)(])")
q=re.compile("\s(\s)*")

with open("TAMIL_TRAIN","r") as f:
    with open("temp","w") as g:
        for sent in f:
            sent=re.sub(p,"",sent)
            sent=re.sub(q," ",sent)
            print(sent,file=g)
        os.remove("TAMIL_TRAIN")
        os.rename("temp","TAMIL_TRAIN")