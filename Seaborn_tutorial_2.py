# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 11:35:42 2022

@author: KIIT
"""
import seaborn as sns
#CTEOGORICAL FEATURES
#countplot
df=sns.load_dataset("tips")
print(df.head())
print(sns.countplot('day',data=df))
print(sns.countplot(y='sex',data=df))
#Barplot
print(sns.barplot(x='total_bill',y='smoker',data=df))
print(sns.barplot(x='sex',y='total_bill',data=df))
#Boxplot
print(sns.boxplot(x='day', y='total_bill',data=df))
print(sns.boxplot('smoker','total_bill',data=df))
print(sns.boxplot(x='day', y='total_bill',data=df,palette='rainbow'))
print(sns.boxplot(data=df,orient='v'))
#Violinplot
print(sns.violinplot(x='total_bill',y='day',data=df))
print(sns.violinplot(x='total_bill',y='day',data=df,palette='rainbow'))