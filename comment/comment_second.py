import pandas as pd
import csv
# ck = pd.read_csv('../JData_Comment.csv')
# # print ck
# dk = ck.drop_duplicates(['sku_id'])
# dk = dk.drop(['dt'],axis=1)
# dk.to_csv('Comment.csv',index=False)

read = csv.reader(open('myJData_Comment.csv'))
read2 = csv.reader(open('JData_Product.csv'))
write = csv.writer(open('myJData_Comment.csv','a',newline=''))

g = []
t = []
for r in read:
    g.append(r[0])
for r in read2:
    if r[0] not in g:
        write.writerow([r[0],0,0,0])
# print len(t)