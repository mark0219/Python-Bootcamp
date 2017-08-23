# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 14:24:30 2017

@author: JRBRAD
"""

f_in = open('../data/tuples.txt','r')

text = f_in.readlines()

for line in text:
    for element in line.split(','):
        print int(element.rstrip('\n'))