# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 10:14:00 2022

@author: KIIT
"""

num_list=[10,20,30]
num_list2=[5,2,3]
add=[]
sub=[]
multi=[]
div=[]
mod=[]
expon=[]
for j in range(3):
  add.append(num_list[j]+num_list2[j])
  add.append(num_list[j]-num_list2[j])
  add.append(num_list[j]*num_list2[j])
  add.append(num_list[j]/num_list2[j])
  add.append(num_list[j]%num_list2[j])
  add.append(num_list[j]**num_list2[j])
  
  print("\n The list items after add= ",add)
  print("\n The list items after sub= ",sub)
  print("\n The list items after multi= ",multi)
  print("\n The list items after div= ",div)
  print("\n The list items after mod= ",mod)
  print("\n The list items after expo= ",expon)
  
 