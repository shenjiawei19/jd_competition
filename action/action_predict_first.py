import pickle

import pandas as pd
action = pd.read_csv('../JData_Action_201604.csv')
# action = pandas.read_csv('../demo.csv')
action.time = action.time.map(lambda x:x[:10])
ck =action.groupby(['user_id','sku_id','time','type']).count().reset_index()
ck =ck.drop(['model_id','cate'],axis=1)
ck= ck.groupby(['user_id','sku_id','time','type'])['brand'].sum().unstack()
# print ck
ck = ck.reset_index().fillna(0)
# print ck
# exit()
df = ck[(ck['time']>='2016-04-06')&(ck['time']<='2016-04-10')]
# df = ck[(ck['time']=='2016-04-10')]

u = pd.read_csv('../user/user_feature.csv')
comment = pd.read_csv('../comment/comment_product.csv')
df3 = pd.merge(u,df,how = 'inner',on='user_id')
df4 = pd.merge(comment,df3,how = 'inner',on='sku_id')
df5 = df4.drop(['time'],axis=1)
mid = df5['user_id']
df5.drop(labels=['user_id'], axis=1,inplace = True)
# df5.drop(labels=['user_id', 'other', '16-25age', '26-35age', '36-45age',
#                  '46-55age', '0sex', '1sex', '2sex', '0lv', '1lv', '2lv', '3lv', '4lv', '5lv'], axis=1,inplace = True)
df5.insert(0, 'user_id', mid)
# print df5
# exit()
df5.to_csv('predict1.csv',index=False)