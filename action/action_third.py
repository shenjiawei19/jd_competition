import pandas as pd
def action_third(start_time,end_time):
    df = pd.read_csv('myresult')
    df = df[(df['time'] <= end_time) & (df['time'] >= start_time)]
    u = pd.read_csv(r'C:\project\jd\py3xgb\user\user_feature.csv')
    comment = pd.read_csv(r'C:\project\jd\py3xgb\comment\comment_product.csv')
    df3 = pd.merge(u,df,how = 'inner',on='user_id')
    df4 = pd.merge(comment,df3,how = 'inner',on='sku_id')
    sku_id = df4['sku_id']
    user_id = df4['user_id']
    time = df4['time']
    df5 = df4.drop(['sku_id','user_id','time'],axis=1)
    df5.insert(0, 'time', time)
    df5.insert(0, 'sku_id', sku_id)
    df5.insert(0, 'user_id', user_id)
    df5.to_csv('result.csv',index=False)
    print ('end action_third')

if __name__ == '__main__':
    print (action_third('2016-03-02','2016-03-26'))