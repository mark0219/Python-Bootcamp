# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 20:48:43 2017

@author: jrbrad
"""

max_hours = 40.0
hours = raw_input('Enter Hours: ')
rate = raw_input('Enter Rate: ')
print 'Pay: ', min(float(hours),max_hours) * float(rate) + 1.5 * float(rate) * max(float(hours) - max_hours, 0)