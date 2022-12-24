# -*- coding: utf-8 -*-
"""
Created on Mon May  9 09:15:05 2022

@author: KIIT
"""

def calc(x,y):
    pro=1
    sum=0
    sub=0
    div=0;
   
    sum=x+y
    pro=x*y
    sub=x-y
    div=x/y
        
    return (sum,pro,div,sub)
def main():
        [s,p,div,sub]=calc(10,20)
        print("sum is: ", s)
        print("product is: ",p)
        print("division is: ",div)
        print("subsrtaction is: " ,sub)
       
        return
main()
    
     
    