# -*- coding: utf-8 -*-
"""
Created on Mon May  9 09:54:10 2022

@author: KIIT
"""
import re

def isvalid(s):
    pattern =re.compile("(0|91)?[7-9][0-9]{9}")
    return pattern.match(s)  
s=input ("Enter the number:")  
if(isvalid(s)) :
  print("valid number")      
else:
  print("invalid number")     
    