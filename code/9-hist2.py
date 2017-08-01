# -*- coding: utf-8 -*-
"""
Created on Fri Jul 01 13:26:42 2016

@author: james.bradley
"""

myList = [0,1,3,5,2,3,1,0,0,3,4,5]
hist = {}

for thisElement in myList:
    hist[thisElement] = hist.get(thisElement,0) + 1
        
print hist