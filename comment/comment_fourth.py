import pandas as pd

cf = pd.read_csv('comment_feature.csv')
pf = pd.read_csv('../product/product_feature.csv')
# print cf.columns
# print pf
df = pd.merge(pf,cf,how='inner',on='sku_id')
# df = df.loc[:,['sku_id','rate','0cm','1cm','2-10cm','11-50cm','50cm','0bcm','1bcm']]
df.to_csv('comment_product.csv',index=False)

