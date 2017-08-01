# -*- coding: utf-8 -*-
"""
Created on Tue May 23 21:23:21 2017

@author: jrbrad
"""

g = lambda x: True if x % 2 == 0 else False
evens = [x for x in range(50) if g(x)]
print evens