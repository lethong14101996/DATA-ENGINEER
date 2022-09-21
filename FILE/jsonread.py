import json
import pandas.io.json as pd_JSON

with open("data.JSON","r") as f:
    data=json.load(f)
print (data['records'][0]['name'])

f=open('data.JSON','r')
data=pd_JSON.loads(f.read())

df=pd_JSON.json_normalize(data,record_path='records')
print (df.head(2).to_json())
print (df.head(2).to_json(orient='records'))