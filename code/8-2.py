# -*- coding: utf-8 -*-
"""
Created on Mon Jun 05 16:13:28 2017

@author: jrbrad
"""

this_list = []
for i in range(10):
    this_list.append(i)
    
that_list = []
for i in range(10):
    that_list.append(i**2)
    
print 'this_list:', this_list
print 'that_list:', that_list

this_list = [i for i in range(10)]
print this_list

