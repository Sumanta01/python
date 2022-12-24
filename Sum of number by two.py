# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 19:47:51 2022

@author: KIIT
"""

n=int(input())
sum1=0
sum2=0
for i in range(len(str(n))//2):
    sum1=sum1+int(str(n)[i])
for i in range(len(str(n))//2,len(str(n))):
    sum2=sum2+int(str(n)[i])
if(sum1==sum2):
    print("Yes")
else:
    print("No")