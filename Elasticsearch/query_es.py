from elasticsearch import Elasticsearch
es = Elasticsearch()

doc={"query":{"match_all":{}}}

res=es.search(index="users",body=doc,size=10)

#print(res['hits']['hits'])

#for doc in res['hits']['hits']:
#   print(doc['_source'])


from pandas.io.json import json_normalize

df=json_normalize(res['hits']['hits'])
print (df)
#doc={"query":{"match":{"name":"Ronald Goodman"}}}
#res=es.search(index="users",body=doc,size=10)
#print(res['hits']['hits'][0]['_source'])

res=es.search(index="users",q="name:Ronald",size=10)
print(res['hits']['hits'][0]['_source'])


doc={"query":{"match":{"city":"Lake Jonstad"}}}
res=es.search(index="users",body=doc,size=10)
print(res['hits']['hits'])
