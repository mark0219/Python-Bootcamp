# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 21:48:33 2017

@author: jrbrad
"""

def check_data(val):
    data_valid = True
    try:
        val = float(val)
    except:
        if val <> 'done':
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
    
numbers = []
while True:
    number = get_data('Enter a Number: ')
    if number == 'done':
        print sum(numbers), len(numbers), float(sum(numbers))/len(numbers)
        break
    else:
        numbers.append(number)