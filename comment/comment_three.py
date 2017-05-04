# -*- coding: utf-8 -*-
import ast
import csv
from sklearn.feature_extraction import DictVectorizer
from sklearn import preprocessing
from sklearn import tree
fd = open('myJData_Comment.csv')
info = csv.reader(fd)
headers = info.__next__()
write = csv.writer(open('comment_feature.csv','w',newline=''))
write.writerow(['sku_id','cm0','cm1','cm2','cm3','cm4','bm0','bm1','rate'])

# 将特征值转换
for r in info:
    attr_first = [[1,0,0,0,0],[0,1,0,0,0],[0,0,1,0,0],[0,0,0,1,0],[0,0,0,0,1]
                  ][r[1] == '0' and 0 or r[1] == '1' and 1 or r[1] == '2' and 2 or  r[1] == '3' and 3 or  r[1] == '4' and 4]
    attr_second = [[1,0],[0,1]][r[2] == '1' and 1]
    # attr_third = [[1,0,0,0,0,0],[0,1,0,0,0,0],[0,0,1,0,0,0],[0,0,0,1,0,0],[0,0,0,0,1,0],[0,0,0,0,0,1]][
    #     float(r[3]) == 0 and 1 or 0.02>float(r[3]) >= 0.01 and 2 or
    #     0.03>float(r[3]) >= 0.02 and 3 or 0.04>float(r[3]) >= 0.03 and 4 or
    #     float(r[3]) >= 0.04 and 5]
    write.writerow([r[0]]+attr_first+attr_second+[r[3]])
