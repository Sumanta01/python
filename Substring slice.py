# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 01:19:14 2022

@author: KIIT
"""
str1="ABCD"
str2="CDAB"

def if_rotaion(str1,str2):
      x=str1[:1]
      y=str2[:1]
      for i in range (len(str1)):
          if str1[i:i+1]==y:
             newstr=str1[i:]+str1[:i]
             if newstr==str2:
                return 1
             else:
                 return 0
print(if_rotaion(str1,str2))