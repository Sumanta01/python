# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 10:11:08 2022

@author: KIIT
"""

str1=input("Enter the string:")
total=1;
for i in range(len(str1)):
    if(str1[i]==' ' or str1=='\n' or str1=='\t'):
        total=total+1
print("The total numbers of words in string= ",total)
        