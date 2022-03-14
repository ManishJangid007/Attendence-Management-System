from ServerSide.Connection import Connection

class SelectOperation():
    def __init__(self):
        obj = Connection
        self.conn = obj.connect()
        self.cur = self.conn.cursor()


    def verifyTeacher(self, user_name, password):
        try:
            query = "SELECT * FROM Teachers WHERE user_name = %s AND password = %s"
            value = [user_name, password]
            self.cur.execute(query, value)
            result = self.cur.fetchone()
            if result:
                return True
            else:
                return False
        except:
            pass