# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 09:24:21 2022

@author: KIIT
"""

marks={}.fromkeys(['math','english','science'],0)
print(marks)
for item in marks.items():
    print(item)
    print(list(sorted(marks.keys())))