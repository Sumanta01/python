# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 21:20:05 2022

@author: KIIT
"""

n=int(input("Enter the number:"))
sum=0
if(n//10!=0):
    sum=0
while(n!=0):
    r=n%10
    sum+=r
    n=n//10
    n==sum
    print("sum is {1}",sum)
  
      