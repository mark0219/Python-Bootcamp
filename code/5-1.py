# -*- coding: utf-8 -*-
"""
Created on Wed Jul 06 09:10:09 2016

@author: james.bradley
"""

dim = 10
row = [1] * dim
matrix = [row] * dim
print matrix
print

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if j <= i:
            print matrix[i][j]
        else:
            print
            break