from db_utils import db_connect

con = db_connect()
cur = con.cursor()

cur.execute("DROP TABLE IF EXISTS configuration")
configuration_sql = """
 CREATE TABLE configuration  (
     id integer PRIMARY KEY,
     hot_threshold integer NOT NULL)"""
cur.execute(configuration_sql)

insert_sql = "INSERT INTO configuration (id, hot_threshold) VALUES (?, ?)"
cur.execute(insert_sql, (1, 25))
