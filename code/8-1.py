# -*- coding: utf-8 -*-
"""
Created on Fri Jul 01 11:57:08 2016

@author: james.bradley
"""

def del_list(x):
    del x[0]
    
def del_list1(x):
    return x[1:]
    
def del_list_wrong(x):
    x =  x[1:]
    
def chg_int(x):
    x = x+ 1
    
def chg_int_ret(x):
    return x + 1
    
myList = [0,1,2,3]
print 'del_list(' + str(myList) + ')'
del_list(myList)
print myList
print

myList = [0,1,2,3]
print 'del_list1(' + str(myList) +')'
myList = del_list1(myList)
print myList
print

myList = [0,1,2,3]
print 'del_list_wrong(' + str(myList) + ')'
myList = del_list_wrong(myList)
print myList
print

myInt = 5
print 'chg_int(' + str(myInt) + ')'
chg_int(myInt)
print myInt
print

myInt = 5
print 'chg_int_ret(' + str(myInt) + ')'
myInt = chg_int_ret(myInt)
print myInt