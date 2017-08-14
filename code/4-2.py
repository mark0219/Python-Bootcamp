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

costVar = raw_input('Enter variable cost: ')
valid_input1, costVar = check_data(costVar)
    
costFixed = raw_input('Enter fixed cost: ')
valid_input2, costFixed = check_data(costFixed)
    
hoursLabor = raw_input('Enter labor hours: ')
valid_input3, hoursLabor = check_data(hoursLabor)
    
if valid_input1 and valid_input2 and valid_input3  == True:
    costTotal = costFixed + hoursLabor * costVar
    print 'Total cost = ',costTotal
else:
    print "Invalid data"