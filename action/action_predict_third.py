import pickle
import csv
import warnings
from numpy import random as rd, array, int32, float32

fd = open('xgb.bin','rb')
cls = pickle.load(fd)
write = csv.writer(open('predict_result','w',newline=''))
write.writerow(['user_id','sku_id','rate'])
read = csv.reader(open('predict1.csv'))
read.__next__()
# print len(read.next())
# print len(read.next())
# exit()
n= 0
for r in read:

    oneRowX = list(map(float,r[2:]))

    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=DeprecationWarning)
        x = array(oneRowX, dtype=float32)
        # exit()
        # print x.shape
        # exit()
        x.shape = [1, 39]
        predictedY = cls.predict_proba(x)[0][1]
        if predictedY>=0.35:

            write.writerow([r[0], r[1],float(predictedY)])
            n+=1

print (n)