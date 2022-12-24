# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 09:55:50 2022

@author: KIIT
"""
n1=int(input("Enter the number:"))
n2=0
n3=1
c=0
if(n1<=0):
    print("Enter the positive number:")
elif(n1==1):
    print("fibbpnaci series upto ",n1)
    print(n1)
else:
    print("Fibonacci sequence:")
    while(c<n1):
        print(n2)
        n4=n2+n3
        n2=n3
        n3=n4
        c+=1
    


