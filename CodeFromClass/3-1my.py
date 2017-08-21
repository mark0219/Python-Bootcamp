# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 12:54:27 2017

@author: jrbrad
"""

num = raw_input('Enter a number: ')
num = int(num)

if num % 2 == 0:
    print num, ' is even'
else:
    print num, ' is odd'