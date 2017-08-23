# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 10:19:33 2017

@author: JRBRAD
"""

for i in [0, 1, 2]:
    print i

print

for i in range(3):
    print i
    
print

print range(2,21,2)

sum_term = 0
x = float(raw_input('Input x value:'))
for y in range(10):
    sum_term = sum_term + x**y
print sum_term

sum_term = 0
x = float(raw_input('Input x value:'))
for y in range(10):
    sum_term += x**y
print sum_term

keep_going = True
i = 0
while keep_going == True:
    i = i + 1
    if i >= 19:
        keep_going = False
        
print i

i = 0
while i < 19:
    i += 1
print i

x = float(raw_input('Input x value:'))
y = 0
sum_term = 0
while x**y > 0.00000001:
    sum_term += x**y
    y += 1
print sum_term, x**y

x = 0.1
#print x
print "{:10.20f}".format(x)

print('%6.20f' % x)
print('%6.20f %2i' % (x,x))
y = x*100
print('%6.1f' % y + '%')


