# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 10:28:23 2022

@author: KIIT
"""

for num in range(1,101):
    count =0
for i in range(2,num//2+1):
    if(num%i==0):
        count=count+1
        break
    if(count ==0 and num!=1):
      print("%d" %num,end='  ')    
        
     