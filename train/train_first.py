import pandas as pd
action = pd.read_csv('../JData_Action_201604.csv')
# action = pandas.read_csv('../demo.csv')
action.time = action.time.map(lambda x:x[:10])
ck =action.groupby(['user_id','sku_id','time','type']).count().reset_index()
ck =ck.drop(['model_id','cate'],axis=1)
ck= ck.groupby(['user_id','sku_id','time','type'])['brand'].sum().unstack()
# print ck
ck = ck.reset_index().fillna(0)
df = ck[ck['time']>='2016-04-11']
df.to_csv('traindata.csv',index=False)