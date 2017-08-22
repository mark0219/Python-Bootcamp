# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 21:18:25 2017

@author: jrbrad
"""

def computegrade(grade):
    try:
        grade = float(grade)
        if grade < 0  or grade > 1:
            response =  'Grade must be between 0.0 and 1.0'
        elif grade >= 0.9:
            response =  'A'
        elif grade >= 0.8:
            response =  'B'
        elif grade >= 0.7:
            print 'C'
        elif grade >= 0.6:
            response =  'D'
        else:
            response =  'F'
    except:
        response =  'Grade data must be numeric'

    return response
    
grade = raw_input('Please enter a grade between 0.0 and 1.0:')
print computegrade(grade)