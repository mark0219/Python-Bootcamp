# -*- coding: utf-8 -*-
"""
Created on Tue May 23 19:34:05 2017

@author: jrbrad
"""

import os
import re
import matplotlib.pyplot as plt
code_dir = os.path.dirname(__file__)

#f = open('D:/TeachingMaterials/BusinessAnalytics/Programming/Python/BootCamp/2017/PythonBootCamp/newMaterial/HamletSililoquy.txt','r')
f = open(os.path.join(code_dir,'HamletSililoquy.txt'),'r')
fh_dict = {}
word_count = 0
top_items = 15

lines = f.readlines()
for line in lines:
    #line = re.sub('\x92',"'",line)
    #print line
    print line
    line = line.strip()
    words = line.split(' ')
    print words
    for word in words:
        word = word.strip().lower()
        word = re.sub('[.,\/#!$%\^&\*;:{}=\-_`~()\'?]$','',word)
        word = re.sub('^[.,\/#!$%\^&\*;:{}=\-_`~()\'?]','',word)
        word = re.sub("'d",'ed',word)
        word = re.sub("'s",'',word)
        fh_dict[word] = fh_dict.get(word,0) + 1
        word_count += 1
    
print fh_dict

fh_tuple = [(v,k) for k,v in fh_dict.iteritems()]
print fh_tuple

fh_tuple.sort(reverse = True)
print
print fh_tuple
print
print word_count

words = [x[1] for x in fh_tuple]
words = words[:top_items]
freqs = [x[0] for x in fh_tuple]
freqs = freqs[:top_items]
y_pos = range(len(words))

plt.bar(y_pos, freqs, align='center', alpha=0.5)
plt.xticks(y_pos, words)
plt.ylabel('Frequency')
plt.xlabel('Words')
plt.rcParams['figure.figsize'] = [15,9]
 
plt.show()
    
f.close()
