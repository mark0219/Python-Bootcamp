# -*- coding: utf-8 -*-
"""
Created on Tue May 23 21:31:34 2017

@author: jrbrad
"""

my_list = []
for x in range(10):
    my_list.append(2*x)
print my_list
    
print [2*x for x in range(10)]