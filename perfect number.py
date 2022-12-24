# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 09:33:24 2022

@author: KIIT
"""

first=int(input("Enter the  first number:"))
last=int(input("Enter the last number:"))

for n in range(first,last+1):
     sum=0
     for i in range(1,n):
       if(n%i==0):
        sum+=i
     if(n==sum):
      print("The perfect number are{0}:",n)
