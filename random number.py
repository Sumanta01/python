# -*- coding: utf-8 -*-
"""
Created on Wed May 18 10:22:46 2022

@author: KIIT
"""

import random
x=[]
for i in range(10):
    x.append(random.random())
for i in range(10):
    print(x[i])
    for i in range (10):
        print("{:.2f})".format(x[i]))
        