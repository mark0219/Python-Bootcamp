# -*- coding: utf-8 -*-
"""
Created on Mon Jul 04 08:14:45 2016

@author: james.bradley
"""

base = 1.0
counter = 0
diff = True

while diff == True:
    counter += 1
    increment = 1/pow(2.0,float(counter))
    if base + increment > base:
        diff = True
    else:
        diff = False
        
print counter - 1, 1/pow(2.0,counter-1)