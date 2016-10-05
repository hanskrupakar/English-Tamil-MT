# -*- coding: utf-8 -*-
from __future__ import print_function
from indicnlp.morph import unsupervised_morph 
from indicnlp import common
import sys

common.INDIC_RESOURCES_PATH="/opt/indic_nlp_library/indic_nlp_resources"

analyzer=unsupervised_morph.UnsupervisedMorphAnalyzer('ta')

with open(sys.argv[1], 'r') as f:
	with open(sys.argv[1]+'_morph', 'w+') as g:
		for line in f.readlines():
			if line:
				tokens=analyzer.morph_analyze_document(line.decode('utf-8').strip().split(' '))
				print(' '.join(tokens).strip().encode('utf-8'), file=g)
