# -*- coding: utf-8 -*-
"""
Created on Wed May 18 09:53:59 2022

@author: KIIT
"""

import numpy
x=numpy.array([[1,2],[4,6]])
y=numpy.array([[5,4],[8,9]])
print("Sqare root is:")
print(numpy.sqrt(x))
print("The summation of element:")
print(numpy.sum(y))
print("The column wise summation of element:")
print(numpy.sum(y,axis=0))
print("The row wise summation of element:")
print(numpy.sum(y,axis=1))
