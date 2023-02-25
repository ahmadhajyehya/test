import pymysql

# Establishing a connection to DB
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='123', db='db')
conn.autocommit(True)

# Getting a cursor from Database
cursor = conn.cursor()

# Deleting data into table
cursor.execute("DELETE FROM users WHERE id = 1")

cursor.close()
conn.close()
