# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

hours = raw_input('Enter hours: ')
dataOK = True
if not(type(hours) == 'float' or type(hours) == 'int'):
    try:
        hours = float(hours)
    except:
        print 'Cannot interpret input as numerical'
        dataOK = False
        
staffLevel = raw_input('Enter number of workers: ')

if not(type(staffLevel) == 'float' or type(staffLevel) == 'int'):
    try:
        staffLevel = float(staffLevel)
    except:
        print 'Cannot interpret input as numerical'
        dataOK = False
        
if dataOK == True:
    print 'Total person-hours: ', hours * staffLevel