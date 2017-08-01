# -*- coding: utf-8 -*-
"""
Created on Mon Jul 04 08:14:45 2016

@author: james.bradley
"""

int_flag = True
val=1
counter = 1

while int_flag == True:
    counter += 1
    val *=2
    print counter, val, type(val)
    if type(val).__name__ == 'long':
        int_flag = False
        
largest = 0
for i in range(31):
    largest += 2**i
    
print largest, type(largest)
print largest + 1, type(largest+1)