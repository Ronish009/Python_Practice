import psycopg2

conn=psycopg2.connect("postgresql://postgres:ronish@localhost:5432/postgres")
cur=conn.cursor()

query="""
SELECT id, name, embedding
    FROM my_cosine
    ORDER BY embedding <=> %s
    LIMIT 2
"""
cur.execute(query, ("[2,2]",))
f=cur.fetchall()
print(f)
conn.close()