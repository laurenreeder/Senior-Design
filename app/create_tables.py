import psycopg2
from app.globals import local_connect

conn = local_connect()
cursor = conn.cursor()
cursor.execute("DROP TABLE categories")
cursor.execute("DROP TABLE images")
cursor.execute("DROP TABLE datasets")


cursor.execute("CREATE TABLE datasets(name varchar primary key, s3_key varchar, model_updated boolean default false)")
cursor.execute("CREATE TABLE images(id varchar primary key, dataset_name varchar references datasets (name), path varchar, label varchar, prediction varchar, dist_from_surface float)");
cursor.execute("CREATE TABLE categories(category varchar, dataset_name varchar references datasets (name))")


cursor.close()

conn.commit()
conn.close()

