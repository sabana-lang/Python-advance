f=open('data.csv','r')
import csv
r=csv.reader(f)
for i in r:
    print(i)
f.close()       