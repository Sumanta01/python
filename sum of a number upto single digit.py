# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 10:14:03 2022

@author: KIIT
"""

def sum_number(n):
    sum=0
    while(n>0 or sum>9):
        if(n==0):
            n=sum
            sum=0
            sum+=n%10
            n//=10
        return sum
    n=int(input("Enter the number:"))
    print(sum_number(n))
    
    
    
      