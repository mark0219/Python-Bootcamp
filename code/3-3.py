# -*- coding: utf-8 -*-
"""
Created on Fri Jul 01 19:02:36 2016

@author: james.bradley
"""

valid_input = True

costVar = raw_input('Enter variable cost: ')
try:
    costVar = float(costVar)
except:
    valid_input = False
    
costFixed = raw_input('Enter fixed cost: ')
try:
    costFixed = float(costFixed)
except:
    valid_input = False
    
hoursLabor = raw_input('Enter labor hours: ')
try:
    hoursLabor = float(hoursLabor)
except:
    valid_input = False
    
if valid_input == True:
    costTotal = costFixed + hoursLabor * costVar
    print 'Total cost = ',costTotal
else:
    print "Invalid input"