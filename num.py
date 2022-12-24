# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 09:53:18 2022

@author: KIIT
"""
min=int(input("Enter the  min number =  :"))
max=int(input("Enter the  max number =  :"))
print("nAll negative numbers from {0} and {1}".format(min,max))
for num in range(min,max+1):
  if(num<0):
   print(num,end='  ')

