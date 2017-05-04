import pandas
def action_first(file):
    action = pandas.read_csv(file)
    action.time = action.time.map(lambda x:x[:10])
    ck =action.groupby(['user_id','sku_id','time','type']).count().reset_index()
    ck =ck.drop(['model_id','cate'],axis=1)
    ck= ck.groupby(['user_id','sku_id','time','type'])['brand'].sum().unstack()
    ck = ck.reset_index().fillna(0)
    ck.to_csv('action_all.csv',index=False)
    return 'end to first'

if __name__ == '__main__':
    print (action_first('../JData_Action_201602.csv'))