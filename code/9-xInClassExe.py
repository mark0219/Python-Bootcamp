# -*- coding: utf-8 -*-
"""
Created on Fri Jul 01 13:03:39 2016

@author: james.bradley
"""

def del_last_element(x):
    del x[len(x)-1]
    
myList2 = [0,1,2,3,4,5]
print myList2
del_last_element(myList2)
print myList2