import pandas as pd
from action.action_predict_first import action_predict_first
from train.vialid import vialid

# print (action_predict_first('JData_Action_201604.csv', '2016-04-11', '2016-04-15','predict2.csv'))

df = pd.read_csv('predict2.csv')
df2 = df.groupby(by=['user_id','sku_id','attr1','attr2','attr3','attr4','1lv','2lv','3lv','4lv','5lv'
                     ])['1','2','3','4','5','6'].sum().reset_index()
df3 =df2.rename(index=str, columns={"1": "act1", "2": "act2",'3':'act3','4':'act4','5':'act5','6':'act6',
                                    '1lv':'lv1','2lv':'lv2','3lv':'lv3','4lv':'lv4','5lv':'lv5'})


def attr1_4(x):
    if x.attr1 == 1:
        return 4 * (
        (x.act1) * 1.2 + (x.act2) * 33 + (x.act3) * (-20) + (x.act4) * (-1000) + (x.act5) * 1 + (x.act6) * 2.1)
    elif x.attr2 == 1:
        return 6.5 * (
        (x.act1) * 1.2 + (x.act2) * 33 + (x.act3) * (-20) + (x.act4) * (-1000) + (x.act5) * 1 + (x.act6) * 2.1)
    elif x.attr3 == 1:
        return 4.7 * (
        (x.act1) * 1.2 + (x.act2) * 33 + (x.act3) * (-20) + (x.act4) * (-1000) + (x.act5) * 1 + (x.act6) * 2.1)
    elif x.attr4 == 1:
        return 4.0 * (
        (x.act1) * 1.2 + (x.act2) * 33 + (x.act3) * (-20) + (x.act4) * (-1000) + (x.act5) * 1 + (x.act6) * 2.1)
def lv(x):
    if x.lv1 == 1:
        return 0*x.rate
    elif x.lv2 == 1:
        return 0*x.rate
    elif x.lv3 == 1:
        return 3*x.rate
    elif x.lv4 == 1:
        return 2*x.rate
    elif x.lv5 == 1:
        return 2*x.rate

# print(rate)
df3['rate'] = df3.apply(attr1_4,axis=1)
df3['rate2'] = df3.apply(lv,axis=1)


df4 = df3.sort_values(by='rate2', ascending=0).head(1000)
df5 = df4.loc[:, ['user_id', 'sku_id']]
df5 = df5.drop_duplicates(['user_id'])
df5.to_csv('20170506.csv',index=False)