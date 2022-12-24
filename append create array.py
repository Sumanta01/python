# -*- coding: utf-8 -*-
"""
Created on Wed May 11 09:31:06 2022

@author: KIIT
"""

import array
arr=array.array('i',[1,2,3])
print("The new array created is : ",end="")
for i in range(0,3):
    print(arr[i],end="")
    print("\r")
    arr.append(4);
    print("The append arry is : ",end="")
for i in range(0,4):
        print(arr[i],end="")
        arr.insert(2,6)
        print("\r")
        print("\n The append arry is : ",end="")
for i in range(0,6):
        print(arr[i],end="")
        print("\r")
        
        