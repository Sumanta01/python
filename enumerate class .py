# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 09:37:27 2022

@author: KIIT
"""

grocery=('bread','milk','butter')
enumerateGrocery=enumerate(grocery)
print(type(enumerateGrocery))
print(list(enumerateGrocery))
enumerateGrocery=enumerate(grocery,43)
print(list(enumerateGrocery))
