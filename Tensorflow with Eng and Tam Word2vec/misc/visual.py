import random
import numpy as np
import matplotlib 
from matplotlib import pyplot as plt
import pickle
import os
import pylab
matplotlib.rcParams['backend'] = "Qt4Agg"

with open('../dataset/ENGLISH_TRAIN','r') as f:
    x = np.array([a.count(' ') for a in f.readlines()])
with open('../dataset/TAMIL_TRAIN','r') as f:
    y = np.array([a.count(' ') for a in f.readlines()])

plt.figure()  
plt.axis([0, 200, 0, 120000])  

plt.subplots_adjust(hspace=.4)
ax = plt.subplot(2,1,1)
plt.hist(x, bins=10, alpha=0.5, label='English')
plt.hist(y, bins=10, alpha=0.5, label='Tamil')
plt.title('Overlapping')  
plt.xlabel('No. of words')  
plt.ylabel('No of sentences')  
plt.legend() 

common_params = dict(bins=20, 
                     range=(0, 80))

plt.subplot(2,1,2)
plt.title('Skinny shift')
plt.hist((x, y), **common_params)
plt.legend(loc='upper right')
common_params['histtype'] = 'step'
plt.xlabel('No. of words')  
plt.ylabel('No of sentences') 
plt.legend() 
pylab.savefig('Histogram.png', bbox_inches='tight')
plt.show()

plt.subplots_adjust(hspace=.4)
plt.subplot(2,1,1)
plt.title('Scatter - Correlation analysis')
plt.xlabel('English')
plt.ylabel('Tamil')
plt.plot(x,y)

plt.subplot(2,1,2)
plt.xlabel('English')
plt.ylabel('Tamil')
plt.hist2d(x,y,bins=10, range=[[0,70],[0,50]]);
pylab.savefig('Correlation.png', bbox_inches='tight')
plt.show()