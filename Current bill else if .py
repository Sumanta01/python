# -*- coding: utf-8 -*-
"""
Created on Sat May 21 23:33:13 2022

@author: KIIT
"""

cnum=input("Enter the consumer number:")
cname=input("Enter the consumer name:")
mno=input("Enter the meter number:")
pmr=int(input("Enter the previous meter reading:"))
cmr=int(input("Enter the current meter reading:"))
tot_unit=cmr-pmr
if(tot_unit<=100):
    amt=tot_unit*2
elif(tot_unit>100 and tot_unit<=200):
    amt=100*2+(tot_unit-100)*3
elif(tot_unit>200 and tot_unit<=300):
    amt=100*2+100*3+(tot_unit-200)*4.50
elif(tot_unit>300 and tot_unit<=500):
    amt=100*2+100*3+100*4.50+(tot_unit-300)*5.50
else:
    amt=100*2+100*3+100*4.50+200*5.50+(tot_unit-500)*7.00
print("Total amount to pay:",amt)
    