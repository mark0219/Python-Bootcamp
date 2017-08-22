# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 20:48:43 2017

@author: jrbrad
"""

def get_data(prompt):
    data_valid = True
    val = raw_input(prompt)
    try:
        val = float(val)
    except:
        data_valid = False
    return data_valid, val
    
max_hours = 40.0
data_valid_hours, hours = get_data('Enter Hours: ')
data_valid_rate, rate = get_data('Enter Rate: ')
if data_valid_hours and data_valid_rate:
    print 'Pay: ', min(hours,max_hours) * rate + 1.5 * max(hours - max_hours, 0) * rate
else:
    print 'You data entry must be numeric.  Thank you!'