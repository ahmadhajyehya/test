# Establishing a connection to DB
import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='123', db='db')
conn.autocommit(True)

# Getting a cursor from Database
cursor = conn.cursor()

# Inserting data into table
cursor.execute("INSERT into users (name, id) VALUES (‘john', 5)")

cursor.close()
conn.close()
