# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 09:41:12 2022

@author: KIIT
"""

n=int(input("Enter the number:"))
sum=0
rem=0
while(n>0):
    rem=n%10
    sum+=rem
    n=n/10
print("sum of digit is ", int(sum))