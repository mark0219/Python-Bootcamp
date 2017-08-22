# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 20:48:43 2017

@author: jrbrad
"""

def check_data(val):
    data_valid = True
    try:
        val = float(val)
    except:
        data_valid = False
        
    return data_valid, val
    
def get_data(prompt):
    data_valid = False
    while data_valid == False:
        data_in = raw_input(prompt)
        data_valid, data_in = check_data(data_in)
        if not data_valid:
            print 'Your input must be numeric.  Thank you!'
            
    return data_in
    
max_hours = 40.0
hours = get_data('Enter Hours: ')
rate = get_data('Enter Rate: ')
print 'Pay: ', min(hours,max_hours) * rate + 1.5 * max(hours - max_hours, 0) * rate