import os
import psycopg2

#conn = psycopg2.connect(dbname="postgres",user="postgres",password="ronish",host="localhost",port="5432")
#conn = psycopg2.connect("postgresql://postgres:ronish@localhost:5432/postgres")
#database connectivity
os.environ["DATABASE_URL"]="postgresql://postgres:ronish@localhost:5432/postgres"
conn = psycopg2.connect(os.environ["DATABASE_URL"])
print(conn)

cur=conn.cursor()
"""
enables the pgvector extension in your PostgreSQL database if extenison is not enabled
getting error psycopg2.errors.UndefinedObject: type "vector" does not exist, embedding vector(3)
"""
#cur.execute("CREATE EXTENSION vector")

query="""
CREATE TABLE IF NOT EXISTS my_cosine (
    id SERIAL PRIMARY KEY,
    name text,
    embedding vector(2)
    )
"""
cur.execute(query)
conn.commit()
conn.close()
print("Table created successfully")

#https://github.com/andreiramani/pgvector_pgsql_windows/releases
"""
Steps to Create Vector Extension
1. Download vector.v0.8.1-pg17
2. Copy vector.dll from vector.v0.8.1-pg17\lib to C:\Program Files\PostgreSQL\17\lib
3. Copy all the vector file present in vector.v0.8.1-pg17\share\extension to C:\Program Files\PostgreSQL\17\share\extension
4. go to pgadmin4 and disconnect to db and connect the db again
5. Excecute CREATE EXTENSION vector
"""



