"""Insertion of Table"""
import psycopg2

conn=psycopg2.connect("postgresql://postgres:ronish@localhost:5432/postgres")
cur=conn.cursor()
query="""
INSERT INTO my_cosine (name, embedding) VALUES (%s, %s)
"""
cur.execute(query,('row3', [2, 5]))
conn.commit()

print("Inserted Data")
cur.execute("select * from my_cosine")
d=cur.fetchall()
print(d)

conn.close()
