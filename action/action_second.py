import pandas as pd
import datetime

def action_second():
    df = pd.read_csv('action_all.csv')
    df = df[df['4']>=1]
    def zfsjjian(x,n = 1):
        y = x[:-1] + str(int(x[-1]) - n)
        if len(y) > 10:
            sj = datetime.datetime.strptime(x, '%Y-%m-%d') - datetime.timedelta(days=n)
            y = sj.strftime('%Y-%m-%d')
        elif y[-2:] == '00':
            sj = datetime.datetime.strptime(x, '%Y-%m-%d') - datetime.timedelta(days=n)
            y = sj.strftime('%Y-%m-%d')
        elif int(y[-2:]) > 28:
            sj = datetime.datetime.strptime(x, '%Y-%m-%d') - datetime.timedelta(days=n)
            y = sj.strftime('%Y-%m-%d')
        return y
    ac = pd.read_csv('action_all.csv')
    df['time'] = df['time'].apply(lambda x:zfsjjian(x,1))
    df4 = pd.merge(ac,df,how = 'inner',on=['user_id','sku_id','time'])
    df4.columns = ['user_id','sku_id','time','1','2','3','4','5','6','t0','t1','t2','t3','t4','t5']
    df4 = df4.drop(['t0','t1','t2','t3','t4','t5'],axis=1)
    df4.to_csv('result1',index=False)
    df['time'] = df['time'].apply(lambda x:zfsjjian(x,2))
    df4 = pd.merge(ac,df,how = 'inner',on=['user_id','sku_id','time'])
    df4.columns = ['user_id','sku_id','time','1','2','3','4','5','6','t0','t1','t2','t3','t4','t5']
    df4 = df4.drop(['t0','t1','t2','t3','t4','t5'],axis=1)
    df4.to_csv('result2',index=False)
    df['time'] = df['time'].apply(lambda x:zfsjjian(x,3))
    df4 = pd.merge(ac,df,how = 'inner',on=['user_id','sku_id','time'])
    df4.columns = ['user_id','sku_id','time','1','2','3','4','5','6','t0','t1','t2','t3','t4','t5']
    df4 = df4.drop(['t0','t1','t2','t3','t4','t5'],axis=1)
    df4.to_csv('result3',index=False)
    df['time'] = df['time'].apply(lambda x:zfsjjian(x,4))
    df4 = pd.merge(ac,df,how = 'inner',on=['user_id','sku_id','time'])
    df4.columns = ['user_id','sku_id','time','1','2','3','4','5','6','t0','t1','t2','t3','t4','t5']
    df4 = df4.drop(['t0','t1','t2','t3','t4','t5'],axis=1)
    df4.to_csv('result4',index=False)
    df['time'] = df['time'].apply(lambda x:zfsjjian(x,5))
    df4 = pd.merge(ac,df,how = 'inner',on=['user_id','sku_id','time'])
    df4.columns = ['user_id','sku_id','time','1','2','3','4','5','6','t0','t1','t2','t3','t4','t5']
    df4 = df4.drop(['t0','t1','t2','t3','t4','t5'],axis=1)
    df4.to_csv('result5',index=False)
    ck1 = pd.read_csv('result1')
    ck2 = pd.read_csv('result2')
    ck3 = pd.read_csv('result3')
    ck4 = pd.read_csv('result4')
    ck5 = pd.read_csv('result5')
    ck_all = ck1.append(ck2, ignore_index=True)
    ck_all = ck_all.append(ck3, ignore_index=True)
    ck_all = ck_all.append(ck4, ignore_index=True)
    ck_all = ck_all.append(ck5, ignore_index=True)
    # print ck_all
    ck_all =  ck_all.drop_duplicates(['user_id','sku_id','time'])
    # print ck_all
    result = pd.merge(ac,ck_all,how = 'left',on=['user_id','sku_id','time'])
    result.columns = ['user_id','sku_id','time','1','2','3','4','5','6','result','t1','t2','t3','t4','t5']
    result.loc[~result['result'].isnull(),'result']=1
    df4 = result.drop(['t1','t2','t3','t4','t5'],axis=1)
    df4 = df4.fillna(0)
    df4.to_csv('myresult',index=False)
    return "end second"

if __name__ == '__main__':
    print (action_second())



