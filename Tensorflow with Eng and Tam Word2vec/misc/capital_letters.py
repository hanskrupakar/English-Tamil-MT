from __future__ import print_function
import re

with open("Dataset/ENGLISH_TEST","r") as f:
    ip = f.read()
    ip=ip.lower()
    ip=ip.replace("_number","_NUMBER")
    
with open("Dataset/ENGLISH_TEST","w") as f:
    print(ip,file=f)