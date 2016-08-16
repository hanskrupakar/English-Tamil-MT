import sys

with open(sys.argv[1], 'r+') as f:
	o = f.read().lower()
	f.seek(0)
	f.write(o)
	f.truncate()