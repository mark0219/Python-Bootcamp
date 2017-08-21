# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 11:49:58 2017

@author: jrbrad
"""

f = raw_input('Input a Fahrenheit temeperature to convert:')
valid_data = True
try:
    f = float(f)
except:
    valid_data = False
    

if valid_data:
    c = (f - 32.0) * 5 / 9
    print '\nThe temperature ', f, ' degrees Fahrenheit converts to ', c, 'degrees Celsius'
else:
    print "Please enter numerical data."