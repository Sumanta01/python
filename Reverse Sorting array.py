# -*- coding: utf-8 -*-
"""
Created on Wed May 11 10:04:48 2022

@author: KIITy
"""

import array as arr
array1=arr.array('d',[203,54,5,65,7,88,45,76,54.34])
for x in array1:
    print(x)
    
y=array1.tolist()
y.sort()
print(y)
y.sort(reverse=True)
print(y)