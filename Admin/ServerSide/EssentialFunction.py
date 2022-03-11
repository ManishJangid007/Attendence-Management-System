from Connection import Connection
from datetime import date, timedelta, datetime

class EssentialFunction():
    def __init__(self):
        obj = Connection()
        self.conn = obj.connect()
        self.cur = self.conn.cursor(buffered=True)

    def backupAttendance(self):
        try:
            self.cur.execute("SELECT DISTINCT(date) FROM Attendance")
            table_name = self.cur.fetchall()
            if table_name:
                delete = '-'
                for i in range(0, len(table_name)):
                    backup_table = table_name[i][0]
                    if table_name[i][0] != str(date.today()):
                        for c in delete:
                            backup_table = backup_table.replace(c, '')
                        backup_table = 'd' + backup_table
                        query = "CREATE TABLE backupamsx505.{backup_table} AS SELECT student_id, present, absent, year, subject_id, course_id, teacher_id FROM Attendance where date = %s".format(backup_table=backup_table)
                        value = [table_name[i][0]]
                        self.cur.execute(query, value)
                        query = "DELETE FROM Attendance WHERE date = %s"
                        value = [table_name[i][0]]
                        self.cur.execute(query, value)
                        self.conn.commit()
                return True
            else:
                return False
        except Exception as e:
            print(e)

    def updateAge(self, dob, student_id):
        try:
            temp = dob.split('-')
            dd = temp[0]
            mm = temp[1]
            yyyy = temp[2]
            dob = date(int(yyyy), int(mm), int(dd))
            today = date.today()
            age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
            query = "UPDATE Students set age = %s WHERE Student_id = %s"
            value = [age, student_id]
            self.cur.execute(query, value)
            self.conn.commit()
            return age
        except:
            pass
