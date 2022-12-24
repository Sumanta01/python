# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 09:27:36 2022

@author: KIIT
"""

i=0
a='good morning all'
while i<len(a):
    if a[i]=='m':
       i=i+1
       break
print("Current letter",a[i])
i+=1