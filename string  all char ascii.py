# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 09:17:25 2022

@author: KIIT
"""

str1=input("Enter the string:")
for i in range(len(str1)):
    print("The ASCII value of charactar  %c=%d" %(str1[i],ord(str1[i])))