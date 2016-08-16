import sys

s=''
c=0
with open(sys.argv[1], 'r+') as f:
	for line in f.readlines():
		c+=1
		if (len(line.split(' ')) < int(sys.argv[2])):
			s+=line.strip()+'\n'
with open('clean.'+sys.argv[1], 'w+') as f:
	f.write(s)
print 'Source (' + sys.argv[1] + ') :%ld sentences' % (c)
print 'Destination (clean.' + sys.argv[1] + ') :%ld sentences' % (len(s.split('\n')))