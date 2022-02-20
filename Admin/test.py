import mysql.connector

try:
    mydb = mysql.connector.connect(
        # Database Configuration
        # 192.168.137.1
        # database="amsx505",
        host="localhost",
        user="root",
        password=""
    )
    print(mydb)
    mydb.cursor()
    conn = True
except Exception as e:
    print(e)
    conn = False

if conn:
    print("connected")
else:
    print("try again")