import psycopg2 as db
import pandas as pd

conn_string="dbname= 'dataengineering' host='10.1.12.248' user='postgres' password='Lethong14101996'"
conn=db.connect(conn_string)

df=pd.read_sql("select * from users", conn)

print(df)

print(df.to_json(orient='records'))