# -*- coding: utf-8 -*-
import csv

fd = open('../JData_Product.csv')
info = csv.reader(fd)
headers = info.__next__()
# write = csv.writer(open('comment_feature.csv','w',newline=''))
fd2 = open('product_feature.csv','w',newline='')
write = csv.writer(fd2)
write.writerow(['sku_id','attr1','attr2','attr3','attr4','attr5','attr6','attr7','attr8','attr9','attr10'])

# 将特征值转换
for r in info:
    attr_first = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]][r[1] == '1' and 1 or r[1] == '2' and 2 or r[1] == '3' and 3]
    attr_second = [[1,0,0],[0,1,0],[0,0,1]][r[2] == '1' and 1 or r[2] == '2' and 2]
    attr_third = [[1,0,0],[0,1,0],[0,0,1]][r[3] == '1' and 1 or r[3] == '2' and 2]
    write.writerow([r[0]]+attr_first+attr_second+attr_third)

