# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 10:03:57 2017

@author: JRBRAD
"""
import math
dist = lambda x1,y1,x2,y2: math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print dist(0,0,3,4)