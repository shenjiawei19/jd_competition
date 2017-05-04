import csv

fd = open(r'predict1.csv', 'r')
rd = csv.reader(fd)
print (rd.__next__())
print (rd.__next__())
exit()
write = csv.writer(open('new_predict.csv','w',newline=''))
write.writerow(['user_id','sku_id','attr1','attr2','attr3','attr4','attr5','attr6','attr7','attr8','attr9','attr10',
                'cm0','cm1','cm2','cm3','cm4','bm0','bm1','rate','other_age','15','16-25','26-35','36-45','46-55','56',
                '0sex','1sex','2sex','1lv','2lv','3lv','4lv','5lv','1','2','3','4','5','6'])

# for r in rd:
    # write.writerow(r[:-6]+act1+act2+act4+act5+act6)