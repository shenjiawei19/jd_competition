import csv
write = csv.writer(open('JData_Action_all.csv','ab+'))
for i in csv.reader(open('JData_Action_201602.csv')):
    write.writerow(i)
for i in csv.reader(open('JData_Action_201603.csv')):
    write.writerow(i)
for i in csv.reader(open('JData_Action_201604.csv')):
    write.writerow(i)