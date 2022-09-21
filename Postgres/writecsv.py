import psycopg2 as db

conn_string="dbname= 'dataengineering' host='10.1.12.248' user='postgres' password='Lethong14101996'"
conn=db.connect(conn_string)
cur=conn.cursor()
conn=db.connect(conn_string)

#f=open('fromdb.csv','w')
#cur.copy_to(f,'users',sep=',')
#f.close()

f=open('fromdb.csv','r')
print(f.read())

