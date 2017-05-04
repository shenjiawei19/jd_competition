import pickle
import csv
import warnings
from numpy import random as rd, array, int32, float32
import pandas as pd
def action_predict_third():
    fd = open('xgb.bin','rb')
    cls = pickle.load(fd)
    write = csv.writer(open('predict_result','w',newline=''))
    write.writerow(['user_id','sku_id','rate'])
    read = csv.reader(open('predict1.csv'))
    read.__next__()
    n= 0
    for r in read:
        oneRowX = list(map(float,r[2:]))

        with warnings.catch_warnings():
            warnings.simplefilter("ignore", category=DeprecationWarning)
            x = array(oneRowX, dtype=float32)
            x.shape = [1, 39]
            predictedY = cls.predict_proba(x)[0][1]
            if predictedY>=0.35:

                write.writerow([r[0], r[1],float(predictedY)])

    df = pd.read_csv('predict_result')
    df = df.sort_values(by='rate', ascending=0)
    df = df.drop_duplicates(['user_id'])
    print (len(df))
    df.to_csv('predict_result-2.csv', index=False)
    return 'end action_predict_third'
if __name__ == '__main__':
    action_predict_third()