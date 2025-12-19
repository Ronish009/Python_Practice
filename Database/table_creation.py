import os
import psycopg2

#conn = psycopg2.connect(dbname="postgres",user="postgres",password="ronish",host="localhost",port="5432")
#conn = psycopg2.connect("postgresql://postgres:ronish@localhost:5432/postgres")
#database connectivity
os.environ["DATABASE_URL"]="postgresql://postgres:ronish@localhost:5432/postgres"
conn = psycopg2.connect(os.environ["DATABASE_URL"])
print(conn)
#enables the pgvector extension in your PostgreSQL database
cur=conn.cursor()
query="""
CREATE TABLE IF NOT EXISTS my_table (
    id SERIAL PRIMARY KEY,
    name text,
    embedding vector(3)
    )
"""
cur.execute(query)
conn.commit()
print("Table created successfully")


