# -*- coding: utf-8 -*-
"""
Created on Wed Jul 06 09:41:36 2016

@author: james.bradley
"""

stores = {0:'Abingdon, VA', 
1:'Alexandria, VA', 
2:'Appomattox, VA', 
3:'Ashland, VA', 
4:'Blacksburg, VA', 
5:'Boones Mill, VA', 
6:'Bristol, VA', 
7:'Buena Vista, VA', 
8:'Charlotte Court House, VA', 
9:'Charlottesville, VA', 
10:'Chincoteague, VA', 
11:'Clinchco, VA', 
12:'Covington, VA', 
13:'Culpeper, VA', 
14:'Danville, VA', 
15:'Farmville, VA', 
16:'Edinburg, VA', 
17:'Fairfax, VA', 
18:'Franklin, VA', 
19:'Front Royal, VA', 
20:'Galax, VA', 
21:'Glasgow, VA', 
22:'Gordonsville, VA', 
23:'Hampton, VA', 
24:'Leesburg, VA'}

dcs = {0:'Sutherland, VA', 1:'Gordonsville, VA', 2:'Newport News, VA', 3:'Blacksburg, VA', 4:'Mechanicsburg, PA', 5:'Wheeling, WV'}

assign = [(0,0), (1,1), (3,2), (5,3), (2,4), (4,5), (4,6), (4,7), (5,8), (2,9), (2,10), (1,11), (1,12), (1,13), (3,14), (1,15), 
(4,16), (3,17), (4,18), (2,19), (2,20), (3,21), (2,22), (1,23), (3,24)]

#Your code goes here
dc_num = raw_input('DC number: ')
dc_num = int(dc_num)

for thisAssign in assign:
    if thisAssign[0] == dc_num:
        print thisAssign, dcs[thisAssign[0]], stores[thisAssign[1]]