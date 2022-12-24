  # -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 11:34:26 2022

@author: KIIT
"""

import numpy as np
my_lst=[1,2,3,4,5]
arr=np.array(my_lst)
print(arr)#indexing in 1D-Array
print(arr[3])
print(arr.shape)
my_lst1=[22,33,55,66]
my_lst2=[12,34,56,78]
my_lst3=[21,32,43,54]
arr1=np.array([my_lst1,my_lst2,my_lst3])
print(arr1)
print(arr1.shape)
print(arr1.reshape(4,3))
print(arr1.reshape(3,4))
print(arr1[0:1,2:3])
print(arr1[0:2,1:3])#indexing in 2D-Array
arr=np.arange(0,15,step=2)
print(np.linspace(1,10,50))
arr2=[2,3,4,5,6,7]
arr3=[]
print(arr2)
arr3=arr2.copy();
print(arr3)
arr[3:]=100
print(arr)
arr2=arr
arr2[3:]=400
print(arr2)
print(arr2<3)
print(arr2[arr2<3])
print(arr[arr2%3])
print(np.ones(5,dtype=int))
print(np.ones((3,4),dtype=int))
print(np.random.rand(3,3))
print(np.random.randn(4,4))



