# -*- coding: utf-8 -*-
import csv
import pickle
import pandas as pd
from sklearn import tree
df = pd.read_csv('result.csv')

df2 = df[(df['result']==1)]

df3 = df2.iloc[:,[0]]
df4 = df2.iloc[:,[1]]
df3 = df3.drop_duplicates(['user_id'])
df4 = df4.drop_duplicates(['sku_id'])
df5 = pd.merge(df,df3,how='inner',on='user_id')

df5.to_csv('result_tmp.csv',index=False)