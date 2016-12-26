import regex as re
import sys

with open(sys.argv[1], 'r') as f:
	
	s = f.read()
	f.seek(0)
    	
    	if(sys.argv[2]=='en'):
		f.write(re.sub(ur"\p{P}+", "", s.lower().decode('utf-8')).encode('utf-8'))
	else:
		f.write(re.sub(ur"\p{P}+", "", s.decode('utf-8')).encode('utf-8'))
	f.truncate()
