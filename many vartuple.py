# -*- coding: utf-8 -*-
"""
Created on Sun May 22 11:55:14 2022

@author: KIIT
"""

def printinfo(*vartuple):
    return vartuple
def main():
    print("Output is ")
    mytuple=printinfo(10)
    print(mytuple)
    mytuple=printinfo(10,20)
    print(mytuple)
    mytuple=printinfo(10,33,44,55,66,"hello")
    print(mytuple)
    for var in mytuple:
        print(var)
        return
main()