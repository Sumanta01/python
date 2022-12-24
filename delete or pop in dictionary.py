# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 10:12:04 2022

@author: KIIT
"""

squares={1:1,3:2,4:4,5:23,6:36}
print(squares.pop(4))
print(squares)
print(squares.popitem())
print(squares)
del squares[5]
print(squares)
squares.clear()
print(squares)
