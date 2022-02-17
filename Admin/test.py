import mysql.connector

try:
    mydb = mysql.connector.connect(
        # Database Configuration
        # 192.168.137.1
        database="",
        host="localhost",
        user="root",
        password=""
    )
    conn = True
except Exception as e:
    print(e)
    conn = False

if conn:
    print("connected")
else:
    print("try again")