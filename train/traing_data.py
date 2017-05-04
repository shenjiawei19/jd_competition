import pandas as pd
df = pd.read_csv('traindata.csv')
# df = df[df['result']==1]
# print df
# exit()
u = pd.read_csv('../user/user_feature.csv')
# result = pandas.read_csv('action201602.csv')
comment = pd.read_csv('../comment/comment_product.csv')
df3 = pd.merge(u,df,how = 'inner',on='user_id')
df4 = pd.merge(comment,df3,how = 'inner',on='sku_id')
sku_id = df4['sku_id']
user_id = df4['user_id']
time = df4['time']
df5 = df4.drop(['sku_id','user_id','time'],axis=1)
df5.insert(0, 'time', time)
df5.insert(0, 'sku_id', sku_id)
df5.insert(0, 'user_id', user_id)
# print df5.columns
# exit()
df5 = df5[(df5['time']>='2016-04-11') & (df5['time']<='2016-04-16') & (df5['4']==1)]
# print len(df5)
# exit()
df6 = df5.loc[:,['user_id','sku_id']]
# df6 = df6.drop_duplicates(['user_id'])
# print df6
# df5 = df5[((df5['3lv'] == 1) | (df5['2lv'] == 1)) & (df5['4']==1) &(df5['2']>=1)]
# df5 = df5[(df5['user_id'] == 211389)]
# print df5
# print df5.columns
# for i in df5.values:
#     print i
df6.to_csv('train_result.csv',index=False)