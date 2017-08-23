# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 15:43:00 2017

@author: JRBRAD
"""

myListInt = [[0,1,2,3],[3,0,1,2],[2,3,0,1]]

for row in range(len(myListInt)):
    for col in range(len(myListInt[row])):
        print myListInt[row][col]
print        
for row in myListInt:
    for element in row:
        print element
        
a = [[0,1,2],[2,0,1],[1,2,0]]
b = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(a)):
    for j in range(len(a[i])):
        b[j][i]=a[i][j]
print a
print b




myList = [[0,1,2],[2,0,1],[1,2,0]]

for row in myList:
    for element in row:
        print element
    print '\n'

print '\n', 'space between results','\n'

myList[1] = ['zero', 'one']

for row in myList:
    for element in row:
        print element
    print '\n'

