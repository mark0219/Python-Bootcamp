# -*- coding: utf-8 -*-
"""
Created on Tue May 23 19:34:05 2017

@author: jrbrad
"""

import os
import re
code_dir = os.path.dirname(__file__)

#f = open('D:/TeachingMaterials/BusinessAnalytics/Programming/Python/BootCamp/2017/PythonBootCamp/newMaterial/HamletSililoquy.txt','r')
f = open(os.path.join(code_dir,'rbc.txt'),'r')

lines = f.readlines()
for line in lines:
    print line