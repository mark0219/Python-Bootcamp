# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 11:49:58 2017

@author: jrbrad
"""

f = float(raw_input('Input a Fahrenheit temeperature to convert:'))
c = (f - 32.0) * 5 / 9
print '\nThe temperature ', f, ' degrees Fahrenheit converts to ', c, 'degrees Celsius'