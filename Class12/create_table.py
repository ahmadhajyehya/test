# Establishing a connection to DB
import pymysql

connection = pymysql.connect(host='sql12.freemysqlhosting.net', port=3306, user='user', passwd='pass', db='mydb')

# create a cursor object to execute queries
cursor = connection.cursor()
cursor.execute("CREATE TABLE users(id INT NOT NULL,name VARCHAR(45) NOT NULL, PRIMARY KEY (id));")
connection.commit()
cursor.close()
connection.close()
