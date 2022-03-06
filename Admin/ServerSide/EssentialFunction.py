from Connection import Connection


class EssentialFunction():
    def __init__(self):
        obj = Connection()
        self.conn = obj.connect()
        self.cur = self.conn.cursor(buffered=True)

    def BackupAttendance(self):
        try:
            self.cur.execute("SELECT date FROM Attendance")
            table_name = self.cur.fetchone()
            if table_name:
                query = "CREATE TABLE %s (SELECT student_id, present, absent, year, subject_id, course_id, teacher_id FROM Attendance where date = %s)"
                value = [table_name[0], table_name[0]]
                self.cur.execute(query, value)
                data = self.cur.fetchall()
                print(data)
            else:
                print("Table is Empty")
        except Exception as e:
            print(e)
