# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 03:13:23 2022

@author: KIIT
"""

import numpy as np
import pandas as pd
df=pd.DataFrame(np.arange(0,20).reshape(5,4),index=['row1','row2','row3','row4','row5'],columns=['column1','column2','column3','column4'])
print(df.head())
print(df[['column1','column2']])
print(type(df.head))
print(df.loc['row2'])
print(type(df.loc['row2']))
print(df.iloc[:,:])
print(df.iloc[0:3,1:3])
#convert data frame into arrays
print(df.iloc[:,:].values)
print(df.isnull().sum())
print(df['column2'].value_counts())
print(df['column2'].unique())