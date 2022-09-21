from faker import Faker
import csv
output=open('data.CSV','w')
fake=Faker()
header=['name','age','street','city','state','zip','lng','lat']
mywriter=csv.writer(output)
mywriter.writerow(header)

for r in range(1000):
    mywriter.writerow([fake.name(),fake.random_int(min=18,max=80, step=1), fake.street_address(), fake.city(),fake.state(),fake.zipcode(),fake.longitude(),fake.latitude()])
output.close()

# read csv fille
with open('data.csv') as f:
    myreader = csv.DictReader(f)
    header = next(myreader)
    for row in myreader:
        print (row['age'])


import pandas as pd

df = pd.read_csv('data.CSV')
print (df.head(100))


data={'Name':['Paul','Bob','Susan','Yolanda'],'Age':[23,45,18,21]}
df = pd.DataFrame(data)
df.to_csv('fromdf.CSV',index=False)

