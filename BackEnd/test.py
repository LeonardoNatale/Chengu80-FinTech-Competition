import psycopg2

conn = psycopg2.connect('postgresql://group2:123456@10.240.61.106:5432/group2')

cur = conn.cursor()

# cur.execute("DELETE FROM issuerz")

# cur.execute("SELECT * FROM investors WHERE username='Leo'")

cur.execute("SELECT * from issuerz")
conn.commit()
print(cur.fetchall())
cur.close()
conn.close()



