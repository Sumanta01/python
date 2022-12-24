# -*- coding: utf-8 -*-
"""
Created on Wed May 18 00:13:52 2022

@author: KIIT
"""

a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
c=int(input("Enter the value of c:"))
if(a>=b and a>=c):
    largest=a
elif(b>=c):
    largest=b
else:
    largest=c
    
print("The largest is {0}:",format(largest))