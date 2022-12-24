# -*- coding: utf-8 -*-
"""
Created on Mon May  9 10:12:47 2022

@author: KIIT
"""

def getproduct(n):
    product=1
    
   
    num=str(n)
    for i in num:
        
      product=product*int( i)

    return product
n=int(input("Enter the number: "))
print("The product of the number is:",getproduct(n))
    