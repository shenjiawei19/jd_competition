# -*- coding: utf-8 -*-
import csv
import pickle
from xgboost.sklearn import XGBClassifier

import pandas as pd
from sklearn import tree
import numpy as np
from numpy import float32
# 决策树算法

def action_sixth():
    cv = open(r'result_tmp.csv', 'r')
    # n=0

    info = csv.reader(cv)
    # print (dir(info))
    headers = info.__next__()
    print (headers)
    featureList = []
    labelList = []
    tmpX = []
    tmpY = []
    training_data = []
    # 将特征值转换
    for n,row in enumerate(info):
        one = []
        y =int(float(row[len(row) - 1]))
        if y == 1:
            dummyY = np.array([1])
        else:
            dummyY = np.array([0])
        for i in range(3, len(row)-1):
            one.append(float(row[i]))
        x = np.array(one,dtype=float32)
        tmpX.append(x)
        tmpY.append(dummyY)

    xgb = XGBClassifier( learning_rate=0.05, max_delta_step=0, max_depth=5,min_child_weight=4,
                              n_estimators=300, nthread=-1, subsample=0.6)

    trainX = np.array(tmpX)
    trainY = np.array(tmpY)
    xgb.fit(trainX,trainY)
    fd = open('xgb.bin','wb')
    pickle.dump(xgb,fd)
    return  'end sixth'

if __name__ == '__main__':
    action_sixth()
