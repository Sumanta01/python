# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 10:22:33 2022

@author: KIIT
"""

sum=0
print("Enter the  10 numbers n")
for i in range(1,11):
    num=int(input("Number %d = " %i))
    sum=sum+num
    avg=sum/10
print("The sum of 10 numbers  =  ",sum)
print("The avg of 10 numbers =  ",avg)