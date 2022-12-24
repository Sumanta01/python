# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 09:35:55 2022

@author: KIIT
""" 

# inbuilt function return an
value=ord("A")
print(value)
print(chr(value))
ch=input("please enter the charactar:")
if((ord(ch)>=65 and ord(ch)<=90) or (ord(ch)>=97 and ord(ch)<=122)):
 print("The given charactar ",ch," is an Alphabet")
else:
 print("The given charactar ",ch," is Not an Alphabet")