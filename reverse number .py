# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 09:49:36 2022

@author: KIIT
"""

n=int(input("Enter the number:"))
rev=0
while(n>0):
    rem=n%10
    rev=rev*10+int(rem)
    n=n//10
print("Reverse the number is:",(rev))