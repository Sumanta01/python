# -*- coding: utf-8 -*-
"""
Created on Wed May 11 10:26:09 2022

@author: KIIT
"""

n= int(input("Enter the no .of rows in a matrix: "))
a=[[0 for x in range(n)]for y in range(n)]
for i in range(n):
    for j in range(n):
        a[i][j]=int(input())
    print("\n")
print(a)