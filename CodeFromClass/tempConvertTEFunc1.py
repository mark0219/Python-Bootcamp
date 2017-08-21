# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 11:49:58 2017

@author: jrbrad
"""

def f_to_c(f):
    valid_data = True
    try:
        c = (float(f) - 32.0) * 5 / 9
    except:
        valid_data = False
        c = -273
    return valid_data, c

valid_data, c =  f_to_c(32)
print valid_data, c