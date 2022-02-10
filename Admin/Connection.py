import mysql.connector
import sqlite3

class LocalConnection():
    def __init__(self):
        self.conn = sqlite3.connect("localstorage")
        self.cur = self.conn.cursor()

    def setup(self):
        self.cur.execute('''CREATE TABLE conn_data (conn_id real, ip text, user text, password text)''')
        self.cur.execute("INSERT INTO conn_data VALUES (1, '127.0.0.1', 'root', '')")
        self.conn.commit()

    def set_parameters(self, ip, user, password):
        self.cur.execute("UPDATE conn_data SET ip=:ip, user=:user, password=:password WHERE conn_id=1",{
            "ip": ip,
            "user": user,
            "password": password
        })
        self.conn.commit()

    def get_parameters(self):
        self.cur.execute("SELECT * FROM conn_data WHERE conn_id = 1")
        data = self.cur.fetchone()
        return data


class Connection():
    def __init__(self):
        try:
            data = LocalConnection().get_parameters()
        except:
            LocalConnection().setup()
            data = LocalConnection().get_parameters()
        try:
            self.mydb = mysql.connector.connect(
                # Database Configuration
                database="",
                host=data[1],
                user=data[2],
                password=data[3]
            )
            self.conn = True
        except:
            self.conn = False

        try:
            self.mydb1 = mysql.connector.connect(
                # Database Configuration
                # Change Database Name According to Your Need
                database="test",
                host=data[1],
                user=data[2],
                password=data[3]
            )
            self.connDatabase = True
        except:
            self.connDatabase = False

    def cursor(self):
        return self.mydb.cursor()

    def check(self):
        if self.conn:
            return True
        else:
            return False

    def check_database(self):
        if self.connDatabase:
            return True
        else:
            return False



