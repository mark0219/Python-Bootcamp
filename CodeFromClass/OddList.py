# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 15:22:02 2017

@author: JRBRAD
"""

myList = []

for i in range(1,16,2):
    myList.append(i)
print myList

myList = []

for i in range(1,16):
    if i%2 ==1:
        myList.append(i)
print myList