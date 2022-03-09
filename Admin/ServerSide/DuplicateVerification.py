from Connection import Connection

class DuplicateVerification():
    def __init__(self):
        obj = Connection()
        self.conn = obj.connect()
        self.cur = self.conn.cursor()
        self.msg = True

    def duplicateTeacher(self, user_name):
        try:
            query = "SELECT user_name FROM Teachers WHERE user_name = %s"
            value = [user_name]
            self.cur.execute(query, value)
            data = self.cur.fetchone()
            if data:
                self.msg = False
            else:
                self.msg = True
        except:
            self.msg = False

        return self.msg

    def dublicateCourse(self, name):
        try:
            query = "SELECT name FROM Courses WHERE name = %s"
            value = [name]
            self.cur.execute(query, value)
            data = self.cur.fetchone()
            if data:
                self.msg = False
            else:
                self.msg = True
        except:
            self.msg = False

        return self.msg

