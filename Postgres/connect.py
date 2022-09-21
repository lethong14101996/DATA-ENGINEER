import psycopg2 as db
conn_string="dbname= 'dataengineering' host='10.1.12.248' user='postgres' password='Lethong14101996'"
conn=db.connect(conn_string)
cur=conn.cursor()

query2 = "insert into users (id,name,street,city,zip) values(%s,%s,%s,%s,%s)"
data=(1,'Big Bird','Sesame Street','Fakeville','12345')

cur.mogrify(query2,data)
cur.execute(query2,data)
conn.commit()

