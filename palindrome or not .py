# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 16:29:59 2022

@author: KIIT
"""

n=int(input("Enter the number:"))

temp=n
rev=0
while(n>0):
    rem=n%10
    rev=rev*10+rem
    n=n//10
    
if(temp==rev):
 print("IS a palindrome")
else:
 print("It is not a palindrome")
    
