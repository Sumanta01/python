# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 09:43:50 2022

@author: KIIT
"""
string=input("Enter the string:")

char=input("Enter the string:")
count=0
for i in range(len(string)):
     if(string[i]==char):
         count=count+1
         print("The total number of times ",char,"has occured= ",count)
 