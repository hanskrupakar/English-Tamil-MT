from __future__ import print_function
import re

with open('Corpus/ENGLISH_TEST', 'r') as f:
	s = f.read()

s = re.sub(r'[\[\]\|<>&\'\"]*','', s)

with open('Corpus/test.en','w') as g:
	print(s, file=g)


with open('Corpus/TAMIL_TEST', 'r') as f:
	s = f.read()

s = re.sub(r'[\[\]\|<>&\'\"]*','', s)

with open('Corpus/test.ta','w') as g:
	print(s, file=g)