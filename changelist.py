# -*- coding: utf-8 -*-
"""
Created on Sun May 22 11:21:31 2022

@author: KIIT
"""

mylist=[10,20,30]
def changeme(any_list):
    "This changes as passed list:"
    any_list.append([1,2,3])
    print("Value inside the function",any_list)
    return
changeme(mylist)
print("Value outside the function:",mylist)