import mysql.connector
import socket

mydb=""
cur =""
try:

    mydb = mysql.connector.connect(
        # host=socket.gethostbyname(socket.gethostname()),
        host="192.168.137.1",
        user="client",
        password="amsx505@2022",
        database="amsx505"
    )

    print(mydb.get_server_info())
    cur = mydb.cursor()
    conn = True
except Exception as e:
    print(e)
    conn = False

if conn:
    print("connected")
else:
    print("try again")


cur.execute("SELECT * FROM Students")
result = cur.fetchall()
print(result)