import csv

fd = open(r'result_tmp.csv', 'rb')
rd = csv.reader(fd)
rd.next()
# exit()
write = csv.writer(open('new_result.csv','wb'))
write.writerow(['user_id', 'sku_id', 'time', 'attr1', 'attr2', 'attr3', 'attr4', 'attr5', 'attr6', 'attr7', 'attr8',
                'cm0', 'cm1', 'bm0', 'bm1', 'rate0', 'rate1', 'rate2', 'rate3', 'rate4', 'rate5', 'other_age',
                '16-2546-5556', '26-35', '36-45', '0sex', '1sex', '2sex', 'other_lv', '3lv', '4lv', '5lv',
                'act1_0', 'act1_12', 'act1_35', 'act1_610', 'act1_11', 'act2_0', 'act2_12','act2_3',
                'act4_0', 'act4_1', 'act5_0', 'act5_1','act5_2', 'act6_0', 'act6_12', 'act6_35', 'act6_610', 'act6_11','result'])
# rx = r[]
for r in rd:
    act1 = [[1,0,0,0,0],[0,1,0,0,0],[0,0,1,0,0],[0,0,0,1,0],[0,0,0,0,1]][
        float(r[-7]) == 0 and 0 or 1 <= float(r[-7]) <= 2 and 1 or 3 <= float(r[-7]) <= 5 and 2 or
        6 <= float(r[-7]) <= 8 and 3 or float(r[-7]) >= 9 and 4]
    act2 = [[1,0,0],[0,1,0],[0,0,1]][
        float(r[-6]) == 0 and 0 or float(r[-6]) == 1 and 1 or 2 <= float(r[-6]) and 2]
    act4 = [[1,0],[0,1]][float(r[-4]) == 0 and 0 or 1 <= float(r[-4])]
    act5 = [[1,0,0],[0,1,0],[0,0,1]][
        float(r[-3]) == 0 and 0 or float(r[-3]) == 1 and 1 or 2 <= float(r[-3]) and 2]
    act6 = [[1,0,0,0,0],[0,1,0,0,0],[0,0,1,0,0],[0,0,0,1,0],[0,0,0,0,1]][
        float(r[-2]) == 0 and 0 or 1 <= float(r[-2]) <= 3 and 1 or 4 <= float(r[-2]) <= 8 and 2 or
        9 <= float(r[-2]) <= 13 and 3 or float(r[-2]) >= 14 and 4]
    write.writerow(r[:-7]+act1+act2+act4+act5+act6+[r[-1]])