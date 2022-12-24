# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 10:01:41 2022

@author: KIIT
"""

string=input("Enter the string:")

char=input("Enter the charactar:")
count=0
i=0
while(i<len(string)):
    if(string[i]==char):
        count=count+1
        i=i+1
print("The total number of times ",char,"has occured= ",count)
