import pandas as pd


df = pd.read_csv('predict_result')
df = df.sort_values(by='rate',ascending=0)
df = df.drop_duplicates(['user_id'])
df.to_csv('predict_result-2.csv',index=False)

