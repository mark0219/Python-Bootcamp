# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 14:46:15 2017

@author: JRBRAD
"""

myList = [7, 2, 5, 3, 1, 9, 8]
print type(myList)
print len(myList)

for i in range(len(myList)):
    print myList[i]
    
for element in myList:
    print element
    
myList.append(6)
print len(myList), myList

myList = myList + [11, 12]
print myList

myList.extend([13, 14])
print myList