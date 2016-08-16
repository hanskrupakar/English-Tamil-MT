import sys

i = 0
l1 = []
l2 = []
with open(sys.argv[1], 'r') as f:
	for line in f.readlines():
		i+=1
		if not line.strip():
			l1.append(i) 

if(len(sys.argv)>2):
	with open(sys.argv[2], 'r') as f:
		for line in f.readlines():
			i+=1
			if not line.strip():
				l2.append(i) 

if(len(sys.argv)>2):
	for f, b in zip(l1, l2):
		print(f,b)
else:
	for f in l1:
		print(f)