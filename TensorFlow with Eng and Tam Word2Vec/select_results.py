with open('results', 'r') as f:
	for pair in f.read().split('.....................................'):
		if(pair.count('_UNK')<8 and pair.strip()):
			print pair+'\n.....................................\n'