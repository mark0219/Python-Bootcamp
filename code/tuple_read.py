# -*- coding: utf-8 -*-
"""
Created on Wed Jul 06 10:56:12 2016

@author: james.bradley
"""

file_path = 'D:/TeachingMaterials/BusinessAnalytics/Programming/Python/PythonBootCamp/data/'
file_in = open(file_path + 'tuples.txt','r')
data = []

for thisLine in file_in.readlines():
    print thisLine
    thisLine = thisLine.rstrip('\n')
    thisLine = list(thisLine.split(','))
    print type(thisLine),thisLine
    thisLine = [ int(x) for x in thisLine ]
    print thisLine
    thisLine = tuple(thisLine)
    print thisLine
    #data.append()
    
