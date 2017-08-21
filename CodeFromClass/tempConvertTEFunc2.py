# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 11:49:58 2017

@author: jrbrad
"""

def f_to_c():
    valid_data = True
    try:
        f = raw_input('Input a Fahrenheit temeperature to convert:')
        c = (float(f) - 32.0) * 5 / 9
    except:
        valid_data = False
        c = -999
    return valid_data, c

valid_data, c =  f_to_c()
print valid_data, c