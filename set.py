# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 23:57:08 2022

@author: KIIT
"""

set1=set()
print(type(set1))
set1={1,2,3,5,5,6,3}
print(set1)
set2={2,3,4,5,5,2,4,7}
print(set2)
print(set1.intersection(set2))
print(set1.add(8))
print(set2.add(9))
print(set1)
print(set2)
print(set1.difference(set2))
print(set2.difference(set1))
print(set1.isdisjoint(set2))
print(set2.isdisjoint(set1))