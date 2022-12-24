# -*- coding: utf-8 -*-
"""
Created on Sun May 22 12:31:44 2022

@author: KIIT
"""

def myFun(**kwargs):
    for key,value in kwargs.items():
        print("%s=%s" %(key,value))
print("\n Result of **kwargs")
myFun(name="vicky",info="Your age", age=44)