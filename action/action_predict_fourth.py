import pandas as pd

df = pd.read_csv('predict_result')
df = df.sort_values(by='rate',ascending=0)
df = df.drop_duplicates(['user_id'])
# print len(df)
# del df['rate']
df.to_csv('predict_result-2.csv',index=False)
# print df
# df2 = pd.read_csv('result_exact.csv')
# df3 = pd.merge(df,df2,how='left',on='user_id')
# df3 = df3.fillna(0)
# # print df3
# df4 = df3[df3['sku_id_y']==0]
# del df4['sku_id_y']
# df4.to_csv('predict_result-2.csv',index=False)

