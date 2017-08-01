# -*- coding: utf-8 -*-
"""
Created on Wed Jul 06 11:47:06 2016

@author: james.bradley
"""

file_path = 'D:/TeachingMaterials/BusinessAnalytics/Programming/Python/PythonBootCamp/data/'
file_in = open(file_path + 'list.txt','r')
target_list = []

for thisLine in file_in.readlines():
    print thisLine
    thisLine = [int(x) for x in thisLine.rstrip('\n').split(',')]
    print thisLine
    target_list.append(thisLine)
    
print target_list