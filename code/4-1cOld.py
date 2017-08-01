# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 18:36:36 2016

@author: james.bradley
"""

def check_data(data_in):
    dataOK = True
    if not(type(data_in) == 'float' or type(data_in) == 'int'):
        try:
            data_in = float(data_in)
        except:
            print 'Cannot interpret input as numerical'
            dataOK = False
    return data_in, dataOK
            
dataOK = True
hours = raw_input('Enter hours: ')
hours, dataOK = check_data(hours)

staffLevel = raw_input('Enter number of workers: ')
staffLevel, dataOK = check_data(staffLevel)
        
if dataOK == True:
    print 'Total person-hours: ', hours * staffLevel