from __future__ import print_function
import re

'''
with open('../dataset/ENGLISH_TRAIN','r') as f:
    st = f.read()

st = re.sub('(.)_NUMBER(.)','\1 _NUMBER \2')
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

with open('../dataset/ENGLISH_TRAIN', 'r+') as f:
	o = ''.join(f.readlines())
file=''
with open('../dataset/TAMIL_TRAIN', 'r+') as f:
	t = f.readlines()
for i in t:
	if(i[0].isdigit()):
		file+=i[4:]
	else:
		file+=i

with open('../dataset/TAMIL_TRAIN', 'w') as f:
	print(file,file=f)

file=''
with open('../dataset/ENGLISH_TRAIN', 'r+') as f:
	t = f.readlines()
for i in t:
	if(i[0].isdigit()):
		file+=i[4:]
	else:
		file+=i

with open('../dataset/ENGLISH_TRAIN', 'w') as f:
	print(file,file=f)
'''

import heapq, random

with open('../dataset/ENGLISH_TRAIN', 'r+') as f:
	o = f.readlines()
x = [a.count(' ') for a in o]
print ("ENGLISH: ", heapq.nlargest(10,x))

with open('../dataset/TAMIL_TRAIN', 'r+') as f:
	o = f.readlines()
x = [a.count(' ') for a in o]
print ("TAMIL:   ", heapq.nlargest(10,x))
