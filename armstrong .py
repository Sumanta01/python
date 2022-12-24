# -*- coding: utf-8 -*-
"""
Created on Wed May  4 10:16:39 2022

@author: KIIT
"""

def number(n):
    temp=0
    sum=0
    r=0
   
    temp=n
    while(n>0):
        r=n%10
        sum+=r*r*r
        n=n//10
        
    if(temp==sum):
          print("\n Number is armstrong")
    else:
          print("\n Number is not a armstrong")
          
number(153)
        