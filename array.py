# -*- coding: utf-8 -*-
"""
Created on Wed May 11 09:41:30 2022

@author: KIIT
"""

import array
arr=array.array('i',[2,5,6,7,1])
print("The new array is created  is :",end="")
for i in range (0,5):
    print(arr[i],end="")
    print("The popped element is:",end="")
    print(arr.pop(2))
    