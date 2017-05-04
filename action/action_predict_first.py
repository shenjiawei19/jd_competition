import pickle

import pandas as pd

def action_predict_first(file,start,end):
    action = pd.read_csv(file)
    # action = pandas.read_csv('../demo.csv')
    action.time = action.time.map(lambda x:x[:10])
    ck =action.groupby(['user_id','sku_id','time','type']).count().reset_index()
    ck =ck.drop(['model_id','cate'],axis=1)
    ck= ck.groupby(['user_id','sku_id','time','type'])['brand'].sum().unstack()
    # print ck
    ck = ck.reset_index().fillna(0)
    # print ck
    # exit()
    df = ck[(ck['time']>=start)&(ck['time']<=end)]
    # df = ck[(ck['time']=='2016-04-10')]

    u = pd.read_csv(r'C:\project\jd\py3xgb\user\user_feature.csv')
    comment = pd.read_csv(r'C:\project\jd\py3xgb\comment\comment_product.csv')
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
    return 'end predict first'

if __name__ == '__main__':
    action_predict_first('JData_Action_201604.csv','2016-04-06','2016-04-10')