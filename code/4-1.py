# -*- coding: utf-8 -*-
"""
Created on Fri Jul 01 19:02:36 2016

@author: james.bradley
"""

def check_data(data_in):
    try:
        data_in = float(data_in)
    except:
        print "Cannot convert to numerical data"
    return data_in

costVar = raw_input('Enter variable cost: ')
costVar = check_data(costVar)
    
costFixed = raw_input('Enter fixed cost: ')
costFixed = check_data(costFixed)
    
hoursLabor = raw_input('Enter labor hours: ')
hoursLabor = check_data(hoursLabor)
    
costTotal = costFixed + hoursLabor * costVar
print 'Total cost = ',costTotal