import psycopg2 as db

conn_string="dbname='dataengineering' host='10.1.12.248' user='postgres' password='Lethong14101996'"
conn=db.connect(conn_string)
cur=conn.cursor()

query = "select * from users limit 10"

cur.execute(query)

#for record in cur:
#    print(record)


#cur.fetchmany(10)
data=cur.fetchone()
print(data[0])
print(cur.rownumber)