# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 01:46:18 2022

@author: KIIT
"""

import seaborn as sns
df=sns.load_dataset("tips")
print(df.head())
print(type(df))
print(df.dtypes)
print(df.corr())
print(sns.heatmap(df.corr()))
print(sns.jointplot(x='tip',y='total_bill',data=df,kind='hex'))
print(sns.jointplot(x='tip',y='total_bill',data=df,kind='reg'))
print(sns.pairplot(df))
#smoker
print(sns.pairplot(df,hue='smoker'))
print(df['smoker'].value_counts())
print(sns.distplot(df['tip']))
print(sns.distplot(df['tip'],kde=False,bins=10))

