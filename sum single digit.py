# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 23:23:37 2022

@author: KIIT
"""
import math
def digSum( n):
    sum = 0
     
    while(n > 0 or sum > 9):
     
        if(n == 0):
            n = sum
            sum = 0
         
        sum += n % 10
        n //= 10
     
    return sum
 

n =int(input("Enter the number:"))
print (digSum(n))