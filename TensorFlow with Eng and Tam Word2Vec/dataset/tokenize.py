import regex as re
import sys

with open(sys.argv[1], 'r') as f:
	print re.sub(ur"\p{P}+", "", f.read().decode('utf-8')).encode('utf-8')