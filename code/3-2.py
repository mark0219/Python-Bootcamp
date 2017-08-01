# -*- coding: utf-8 -*-
"""
Created on Fri Jul 01 19:31:40 2016

@author: james.bradley
"""

valid_input = True
costVar = raw_input('Enter variable cost: ')
try:
    costVar = float(costVar)
except:
    valid_input = False
    
print valid_input