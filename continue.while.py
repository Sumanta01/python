# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 09:19:43 2022

@author: KIIT
"""

i=0
a='good morning all'
while i<len(a):
    if a[i]=='o' or a[i]=='a':
       i=i+1
    continue
print("Current letter",a[i])
i+=1