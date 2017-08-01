# -*- coding: utf-8 -*-
"""
Created on Fri Jul 01 19:02:36 2016

@author: james.bradley
"""

def check_data(data_in):
    valid_input = True
    try:
        data_in = float(data_in)
    except:
        valid_input = False
    return valid_input, data_in

valid_input = True

costVar = raw_input('Enter variable cost: ')
valid_input, costVar = check_data(costVar)
    
costFixed = raw_input('Enter fixed cost: ')
valid_input, costFixed = check_data(costFixed)
    
hoursLabor = raw_input('Enter labor hours: ')
valid_input, hoursLabor = check_data(hoursLabor)
    
if valid_input == True:
    costTotal = costFixed + hoursLabor * costVar
    print 'Total cost = ',costTotal
else:
    print "Invalid data"