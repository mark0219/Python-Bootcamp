# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 18:17:04 2016

@author: james.bradley
"""

hours = raw_input('Enter time to do job: ')
hours = float(hours)
if hours <= 2:
    print hours, ' is a short time'
elif hours <= 5:
    print hours, ' is a medium-sized time'
else:
    print hours, ' is a long time'
