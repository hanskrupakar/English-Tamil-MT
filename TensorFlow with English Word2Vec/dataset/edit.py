from __future__ import print_function
import re
import fileinput

f = open('ENGLISH_TRAIN','r')
filedata = f.read()
f.close()

newdata = filedata.replace("_NUMBER_NUMBER","_NUMBER")
newdata = re.sub(r'_NUMBER\$','_NUMBER $',newdata)
newdata = re.sub(r'\$_NUMBER','$ _NUMBER',newdata)
newdata = re.sub(r'\<(.)*\>','',newdata)
newdata = re.sub('_NUMBER_NUMBER','_NUMBER',newdata)
newdata = re.sub('_NUMBER\-_NUMBER','_NUMBER - _NUMBER',newdata)
newdata = re.sub('_NUMBER\._NUMBER','_NUMBER',newdata)
newdata = re.sub('_NUMBER%','_NUMBER %',newdata)
newdata = re.sub('\$_NUMBER','$ _NUMBER',newdata)
newdata = re.sub('_NUMBER\-','_NUMBER - ',newdata)

f = open('ENGLISH_TRAIN2','w')
f.write(newdata)
f.close()

f = open('TAMIL_TRAIN','r')
filedata = f.read()
f.close()

newdata = filedata.replace("_NUMBER_NUMBER","_NUMBER")

newdata = re.sub('_NUMBER_NUMBER','_NUMBER',newdata)
newdata = re.sub('_NUMBER\-_NUMBER','_NUMBER - _NUMBER',newdata)
newdata = re.sub('_NUMBER\._NUMBER','_NUMBER',newdata)
newdata = re.sub('_NUMBER%','_NUMBER %',newdata)
newdata = re.sub('\$_NUMBER','$ _NUMBER',newdata)
newdata = re.sub('_NUMBER\-','_NUMBER - ',newdata)
newdata = re.sub(r'\s(-)*\s',' - ',newdata)

print(newdata)

f = open('TA','w')
f.write(newdata)
f.close()

f = open('TAMIL_TEST','r')
filedata = f.read()
f.close()

newdata = filedata.replace("_NUMBER_NUMBER","_NUMBER")

newdata = re.sub('_NUMBER_NUMBER','_NUMBER',newdata)
newdata = re.sub('_NUMBER\-_NUMBER','_NUMBER - _NUMBER',newdata)
newdata = re.sub('_NUMBER\._NUMBER','_NUMBER',newdata)
newdata = re.sub('_NUMBER%','_NUMBER %',newdata)
newdata = re.sub('\$_NUMBER','$ _NUMBER',newdata)
newdata = re.sub('_NUMBER\-','_NUMBER - ',newdata)
newdata = re.sub(r'\s(-)*\s',' - ',newdata)

f = open('TAMIL_TEST','w')
f.write(newdata)
f.close()
'''
with open("ENGLISH.txt","r") as f:
    with open("ENTAM_EN","w") as g:
        for line in f:
            line = re.sub(r'\<(.)*\>','',line)
            line = re.sub(r'\d(\d)*(,\d)*','_NUMBER', line.rstrip())
            line = re.sub(r'(\d)*\d\.(\d)*','_NUMBER', line.rstrip())
            # line = re.sub(r'\"|=|#|<|>|\(|\)','',line)
            # line = re.sub('_NUMBER_NUMBER','_NUMBER',line)
            # line = re.sub('\_NUMBER\.\_NUMBER','_NUMBER',line)
            # line = re.sub('\_NUMBER\-\_NUMBER','_NUMBER - _NUMBER',line)
            print(line,file=g)
            
with open("corpus.bcn.test.en","r") as f:
    with open("ENTAM(test)_EN","w") as g:
        for line in f:
            line = re.sub(r"<(.)*>","",line)
            line = re.sub(r'\d(\d)*(,\d)*',"_NUMBER", line.rstrip())
            line = re.sub(r'\"|=|#|<|>|\(|\)',"",line)
            line = re.sub("\_NUMBER\_NUMBER","_NUMBER",line)
            line = re.sub("_NUMBER._NUMBER","_NUMBER",line)
            line = re.sub("_NUMBER\-_NUMBER","_NUMBER \- _NUMBER",line)
            print(line,file=g)
            
with open("corpus.bcn.dev.en","r") as f:
    with open("ENTAM(dev)_EN","w") as g:
        for line in f:
            line = re.sub(r"<(.)*>","",line)
            line = re.sub(r'\d(\d)*(,\d)*',"_NUMBER", line.rstrip())
            line = re.sub(r'\"|=|#|<|>|\(|\)',"",line)
            line = re.sub("_NUMBER_NUMBER","_NUMBER",line)
            line = re.sub("_NUMBER._NUMBER","_NUMBER",line)
            line = re.sub("_NUMBER\-_NUMBER","_NUMBER \- _NUMBER",line)
            print(line,file=g)'''