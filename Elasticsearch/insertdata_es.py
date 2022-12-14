from elasticsearch import helpers
from elasticsearch import Elasticsearch
from faker import Faker
fake=Faker()

es = Elasticsearch()
es=Elasticsearch({'127.0.0.1'})

doc={"name": fake.name(),"street": fake.street_address(),"city": fake.city(),"zip":fake.zipcode()}

res=es.index(index="users",doc_type="doc",body=doc)

print(res['result'])

actions = [
    {
        "_index": "users",
        "_type": "doc",
        "_source": {
            "name": fake.name(),
            "street": fake.street_address(),
            "city": fake.city(),
            "zip":fake.zipcode()
            }
    }
    for x in range(998) # or for i,r in df.iterrows()
]

res = helpers.bulk(es, actions)
print(res['result'])