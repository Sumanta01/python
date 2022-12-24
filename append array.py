# -*- coding: utf-8 -*-
"""
Created on Wed May 11 09:27:46 2022

@author: KIIT
"""

import array as arr
array1=arr.array('d',[])
for x in range (10):
    array1.append(x)
    for x in array1:
        print(x)