# -*- coding: utf-8 -*-
"""
Created on Wed May 11 09:50:18 2022

@author: KIIT
"""

import array
arr=array.array("i",[2,3,4,56,87])
print("The new created array is:",end=",")
for i in range (0,5):
    print(arr[i],end=",")
    print("\r")
    print("The index first occurance of  2 is:",end=" ")
    print(arr.index(3))
    arr.reverse()
    print("The array after reversing is: ")
    for i in range (0,5):
        print(arr[i],end=",")