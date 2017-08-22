# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 21:18:25 2017

@author: jrbrad
"""

data_ok = True
grade = raw_input('Please enter a grade between 0.0 and 1.0:')
try:
    grade = float(grade)
    if grade < 0  or grade > 1:
        data_ok = False
        print 'Grade must be between 0.0 and 1.0'
    elif grade >= 0.9:
        print 'A'
    elif grade >= 0.8:
        print 'B'
    elif grade >= 0.7:
        print 'C'
    elif grade >= 0.6:
        print 'D'
    else:
        print 'F'
except:
    print 'Grade data must be numeric'
    data_ok = False