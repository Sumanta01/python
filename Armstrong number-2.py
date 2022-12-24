# -*- coding: utf-8 -*-
"""
Created on Wed May 25 16:48:07 2022

@author: KIIT
"""

n=int(input("Enter the number:"))
temp=n
flag=0
r=0
while(n!=0):
    r=n%10
    flag+=r*r*r
    n=n//10
if(temp==flag):
    print("Number is Armstrong:")
else:
    print("Number is not an Armstrong:")
    
    
 
 


 
 
