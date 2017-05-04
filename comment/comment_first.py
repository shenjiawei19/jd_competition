import pandas

comment = pandas.read_csv('JData_Comment.csv')
ck = comment.drop(['dt'],axis=1)
ck = ck.drop_duplicates(['sku_id'])
ck.to_csv('myJData_Comment.csv',index=False)
# ck.to_csv('result3.csv',index=False)
# comment.time = comment.time.map(lambda x:x[:10])
# ck =action[action.type == 4].groupby(['user_id','sku_id','time','type']).count().reset_index()
# ck =comment.drop(['model_id','cate'],axis=1)
# ck.to_csv('result3.csv',index=False)