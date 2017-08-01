# -*- coding: utf-8 -*-
"""
Created on Mon Jun 05 17:32:18 2017

@author: jrbrad
"""

x5 = {'one':'uno','two':'dos','three':'tres'}

for y in x5:
    print y

print 
    
for key,val in x5.iteritems():
    print key, val

print

keys = x5.keys()
keys.sort()
for key in keys:
    print key, x5[key]
