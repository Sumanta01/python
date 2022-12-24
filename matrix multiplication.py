# -*- coding: utf-8 -*-
"""
Created on Mon May 16 09:14:25 2022

@author: KIIT
"""

x=[[23,4,5],
   [4,55,6],
   [6,44,3]]
y=[[3,4,7],
   [5,77,90],
   [8,6,4]]
result=[[0,0,0],
        [0,0,0],
        [0,0,0]]
for i in range(len(x)):
    for j in range (len(x[0])):
        result[i][j]=x[i][j]+y[i][j]
        for r in result:
            print(r)