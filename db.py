import mysql.connector as mysql

db=mysql.connect(
    host='localhost',
    user='root',
    passwd='adis',
    port=3305,
)

cursor=db.cursor()
cursor.execute("Create Database crm")
