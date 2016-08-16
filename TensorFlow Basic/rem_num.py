from __future__ import print_function
import re

with open('ENGLISH_TRAIN','r') as f:
    st = f.read()

st = re.sub(r'\d\d\d','',st)
st = re.sub('_NUMBER_NUMBER','_NUMBER',st)
st = re.sub('_NUMBER\._NUMBER','_NUMBER',st)
st = re.sub('_NUMBER(.)','_NUMBER \1',st)
st = re.sub('(.)_NUMBER','\1 _NUMBER',st)
st = re.sub('_NUMBER\-_NUMBER','_NUMBER \- _NUMBER',st)

print(st)

with open('ENGLISH_TRAIN','w') as g:
    print(st,file=g)
    
with open('TAMIL_TRAIN','r') as f:
    st = f.read()

st = re.sub(r'\d\d\d','',st)

print(st)

with open('TAMIL_TRAIN','w') as g:
    print(st,file=g)    

