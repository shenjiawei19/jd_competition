import pandas as pd

r1 = pd.read_csv('../action/predict_result-2.csv')
r2 = pd.read_csv('train_result.csv')
print (len(r2))
# r23 = pd.read_csv('train_result_exact.csv')
# print (len(r23))

re = pd.merge(r1,r2,how='inner',on=['user_id'])
# re2 = pd.merge(r1,r23,how='inner',on=['user_id'])
print (len(re))

acc = len(re)*1.0/len(r1)
recall = len(re)*1.0/len(r2)
print ('accacury:',acc)
print ('recall:',recall)
print (6*acc*recall/(5*recall+acc))

# re = pd.merge(r2,r1,how='left',on='user_id')
# re = re.fillna(0)
# re = re[re['sku_id_y']==0]
# print re
# exit()
# del re['sku_id_y']
# # re = pd.merge(re,r1,how='inner',on='user_id')
# del re['sku_id2']
# re.to_csv('20170413.csv',index=False)
