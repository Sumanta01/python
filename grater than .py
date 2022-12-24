# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 10:22:07 2022

@author: KIIT
"""


n1=float(input("Enter the first number: "))
n2=float(input("Enter the second number: "))
n3=float(input("Enter the third number: "))
if(n1>=n2)and(n1>=n3):
 largest=n1
elif(n2>=n3):
 largest=n2
else:
 largest=n3
 print("The largest number is ",largest)
      
    
    