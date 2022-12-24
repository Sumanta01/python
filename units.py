# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 09:12:45 2022

@author: KIIT
"""
units=int(input("Enter the number of units :"))
if(units<50):
  amount=units*2.60
  Surcharge=25
elif(units<=100):
    
  amount=130+((units-50)*3.25)
  surcharge=35
elif(units<=200):
  amount=130+162.50+((units-100)*5.26)
  Surcharge=45
else:
  amount=130+162.50+526+((units-200)*8.45)
  Surcharge=75
  total=amount+Surcharge
  print("n Electricity Bill= %.2f"  %total)

