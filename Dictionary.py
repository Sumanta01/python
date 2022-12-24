# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 10:39:51 2022
bike
@author: KIIT
"""

my_dict={'bike1':'Fzs','bike2':'Hero honda','bike3':'unicorn','bike4':'Cbz'}
print(type(my_dict))
print(my_dict)
print(my_dict.keys())
print(my_dict['bike2'])
print(my_dict.items())
for x in my_dict:
    print(x)
for x in my_dict.values():
    print(x)
    for x in my_dict.items():
        print(x)
my_dict['bike5']='Glamour'
print(my_dict)
my_dict['bike3']='Pulser'
print(my_dict)