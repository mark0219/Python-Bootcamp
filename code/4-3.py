# -*- coding: utf-8 -*-
"""
Created on Fri Jul 01 10:30:20 2016

@author: james.bradley
"""

def print_me_void(x):
    print x
    
def return_something():
    return 'Hello'
    
def return_something_mult_2(x):
    return 2*x
    
test = print_me_void(2)
print test

test = return_something()
print test

test = return_something_mult_2(7)
print test
print return_something_mult_2(7)