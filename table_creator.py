import sqlite3

connection=sqlite3.connect('data.db')
cursor=connection.cursor()

table_query1="CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY,username VARCHAR,password VARCHAR)"
table_query2="CREATE TABLE IF NOT EXISTS items (name VARCHAR)"
#INTEGER PRIMARY KEY is used as increamental id when new data inserted id increase by 1 automatacly

cursor.execute(table_query1)
cursor.execute(table_query2)

connection.commit()
connection.close()

