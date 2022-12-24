# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 10:06:05 2022

@author: KIIT
"""

last = int(input(" Please Enter the last Value : "))

print("Palindrome Numbers between 10 and %d are : " %(last))
for num in range(10, last + 1):
    temp = num
    reverse = 0
    
    while(temp > 0):
        Reminder = temp % 10
        reverse = (reverse * 10) + Reminder
        temp = temp //10

    if(num == reverse):
        print("%d " %num, end = '  ')