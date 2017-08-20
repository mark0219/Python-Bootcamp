# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 13:22:38 2016

@author: james.bradley
"""

#fprog1 = open('E:\\BusinessAnalytics\\Prereqs\\program2.txt','r')
fprog1 = open('D:\\BusinessAnalytics\\Prereqs\\Python\\CompetencyExam\\program2.txt','r')

ref = (4.0,4,0)

list_tup = []
for line in fprog1:
    thisLine = []
    line1 = line.split(' ')
    print len(line)
    #thisList = []
    #list_tup.append(tuple(line[0],line[1]))
    #i = 0
    x = []
    for item in line1:
        print item.strip()+'    '
        x.append(float(item.strip()))
        #list_tup.append((line[0],line[1]))
        #print item+'    '
        #print line[i]
        #i=i+1
    list_tup.append(tuple((x[0],x[1])))
print list_tup

list_tup_new = []
count = 0
for i in range(len(list_tup)):
    if pow(((list_tup[i][0]-ref[0])**2+(list_tup[i][1]-ref[1])**2),0.5) <= 2.0:
        list_tup_new.append(list_tup[i])
        count = count + 1
        
#print count
print 'length of original list: ',len(list_tup)
print 'length of filtered list: ',len(list_tup_new)
print list_tup_new
        
fprog1.close()
