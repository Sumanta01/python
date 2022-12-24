# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 11:49:18 2022

@author: KIIT
"""

#READ_JSON TO CSV
import pandas as pd
data='{"employee_name":"james","Email":"James@gmail.com","Job_profile":[{"title1":"Team lead","title2":"Devolper"}]}'
df2=pd.read_json(data)
print(df2.head())

print(df2.to_json(orient="records"))
df=pd.read_csv('C:/Users/KIIT/Downloads/annual-enterprise-survey-2021-financial-year-provisional-size-bands-csv.csv')

print(df.head())
df.to_csv('wine.csv')
#convert json to different json format
print(df.to_json(orient="index"))