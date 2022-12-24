# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 03:34:13 2022

@author: KIIT
"""
#List
print(type([]))
# Append into list
my_lst=['phy','chm',123,45,67,'math',87,44]
print(len(my_lst))
print(my_lst.append('swain'))
print(my_lst.append(["don","roy"]))
print(my_lst)
print(my_lst [2:3])
#INSERT  into list
print(my_lst.insert(3 ,"sumanta" ))
print(my_lst.insert(5,"rock" ))
print(my_lst)
# extend
lst2=[1,2,3,5,6]
print(lst2.extend(['jdk',7]))
print(lst2) 
#pop(delete the item from list(LIFO order delete the element last towards))
lst2.pop()
print(lst2)
lst2.pop(5)
print(lst2)
print(min(lst2))
print(max(lst2))
