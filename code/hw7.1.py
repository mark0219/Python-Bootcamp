# -*- coding: utf-8 -*-
"""
Created on Wed Jul 06 11:40:08 2016

@author: james.bradley
"""

file_path = 'D:/TeachingMaterials/BusinessAnalytics/Programming/Python/PythonBootCamp/data/'
file_in = open(file_path + 'tuples.txt','r')
data = []

for thisLine in file_in.readlines():
    print thisLine
    print thisLine.split(',')