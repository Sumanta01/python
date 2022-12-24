# -*- coding: utf-8 -*-
"""
Created on Sun May 22 11:51:08 2022

@author: KIIT
"""

def printinfo(*vartuple):
    print("output is:")
    for var in vartuple:
        print(var)
        return 
printinfo(10);
printinfo(10,70,60,67,"Hello")