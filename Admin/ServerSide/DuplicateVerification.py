from Connection import Connection

class DuplicateVerification:
    def __init__(self):
        obj = Connection
        self.conn = obj.connect()
        self.cut = self.conn.cursor()

    def verifyTeacherUserName(self):
        query 
