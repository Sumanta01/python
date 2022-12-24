# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 10:07:22 2022

@author: KIIT
"""

num=int(input("Enter any number to find divisor:"))
print("The divisor of number = ")
for i in range(1,num+1):
    if(num%i==0):
        print(i)