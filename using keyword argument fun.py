# -*- coding: utf-8 -*-
"""
Created on Mon May  9 09:34:58 2022

@author: KIIT
"""

def myfun(**kwargs):
    for key, value in kwargs.items():
        print("%s = %s"%(key,value))
    print("\nresult of **kwargs")
myfun(name='vicky',info='your age',age=23)
        