# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 13:10:53 2016

@author: james.bradley
"""

#fprog1 = open('E:\\BusinessAnalytics\\Prereqs\\PythonProgram1Data.csv','r')
fprog1 = open('D:\\BusinessAnalytics\\Prereqs\\Python\\CompetencyExam\\PythonProgram1Data.csv','r')

values_list = []

for line in fprog1:
    thisLine = []
    line = line.split(',')
    for item in line:
        #print item.strip()+'    '
        thisLine.append(int(item.strip()))
    values_list.append(thisLine)
    
    print values_list

fprog1.close()

myDict = {}
myDict[0] = 'small'
myDict[1] = 'small'
myDict[2] = 'small'
myDict[3] = 'mid-range'
myDict[4] = 'mid-range'
myDict[5] = 'mid-range'
myDict[6] = 'mid-range'
myDict[7] = 'large'
myDict[8] = 'large'
myDict[9] = 'large'

text_list=[]
for i in range(len(values_list)):
    one_row = []
    for j in range(len(values_list[i])):
        one_row.append(myDict[values_list[i][j]])
    text_list.append(one_row)
    
print text_list

text_list_next=[]
for i in range(len(text_list[0])):
    one_row = []
    for j in range(len(text_list)):
        one_row.append(text_list[j][i])
    text_list_next.append(one_row)
    
print text_list_next