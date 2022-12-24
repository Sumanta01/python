# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 09:43:21 2022

@author: KIIT
"""

grocery=['bread','milk','butter']
for item in enumerate(grocery):
    print(item)
    print('\n')
for count ,item in enumerate(grocery):
    print(count,item)
    print('\n')
    for count,item in enumerate(grocery,100):
        print(count,item)
    