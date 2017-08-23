# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 16:11:50 2017

@author: JRBRAD
"""

f = open('../data/list.txt','r')
text = f.readlines()

matrix = []
for row in text:
    new_row = []
    for element in row.split(','):
        element = element.rstrip('\n')
        new_row.append(int(element))
    matrix.append(new_row)
    
print matrix
f.close()