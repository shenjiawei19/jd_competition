import pandas as pd

def train_first(file,start,end):
    action = pd.read_csv(file)
    action.time = action.time.map(lambda x:x[:10])
    ck =action.groupby(['user_id','sku_id','time','type']).count().reset_index()
    ck =ck.drop(['model_id','cate'],axis=1)
    ck= ck.groupby(['user_id','sku_id','time','type'])['brand'].sum().unstack()
    # ck.iteritems()
    # print ck
    ck = ck.reset_index().fillna(0)
    df = ck[(ck['time']>=start) & (ck['time']>=end) ]
    df.to_csv('traindata.csv',index=False)


    df = pd.read_csv('traindata.csv')
    u = pd.read_csv(r'C:\project\jd\py3xgb\user\user_feature.csv')
    comment = pd.read_csv(r'C:\project\jd\py3xgb\comment\comment_product.csv')
    df3 = pd.merge(u, df, how='inner', on='user_id')
    df4 = pd.merge(comment, df3, how='inner', on='sku_id')
    sku_id = df4['sku_id']
    user_id = df4['user_id']
    time = df4['time']
    df5 = df4.drop(['sku_id', 'user_id', 'time'], axis=1)
    df5.insert(0, 'time', time)
    df5.insert(0, 'sku_id', sku_id)
    df5.insert(0, 'user_id', user_id)

    df5 = df5[(df5['time'] >= start) & (df5['time'] <= end) & (df5['4'] == 1)]

    df6 = df5.loc[:, ['user_id', 'sku_id']]

    df6.to_csv('train_result.csv', index=False)
    return 'end train'

if __name__ == '__main__':
    train_first('JData_Action_201604.csv','2016-04-11','2016-04-15')