from Connection import Connection
from SelectOperation import SelectOperation

class UpdateOperation():
    def __init__(self):
        connect = Connection()
        self.get = SelectOperation()
        self.conn = connect.connect()
        self.cur = self.conn.cursor()
        self.data = []
        self.msg = None

    def deleteAdmin(self, admin_id):
        try:
            query = "SELECT status from Admins where admin_id = %s"
            value = [admin_id]
            self.cur.execute(query, value)
            self.data = self.cur.fetchall()
            if self.data[0][0].upper() == "HIGH":
                self.msg = False
            else:
                query = "DELETE FROM Admins where admin_id = %s"
                value = [admin_id]
                self.cur.execute(query, value)
                self.msg = True
                self.conn.commit()
            return self.msg

        except Exception as e:
            print(e)
            self.msg = False
            self.conn.rollback()

    def deleteTeacher(self, teacher_id):
        try:
            query = "DELETE FROM Teachers where teacher_id = %s"
            value = [teacher_id]
            self.cur.execute(query, value)
            self.msg = True
            self.conn.commit()
        except Exception as e:
            print(e)
            self.msg = False
            self.conn.rollback()
        return self.msg

    def deleteCourse(self, course_id):
        try:
            query = "DELETE FROM Courses where course_id = %s"
            value = [course_id]
            self.cur.execute(query, value)
            self.msg = True
            self.conn.commit()
        except Exception as e:
            print(e)
            self.msg = False
            self.conn.rollback()
        return self.msg

    def deleteSubject(self, subject_id):
        try:
            query = "DELETE FROM Subjects where subject_id = %s"
            value = [subject_id]
            self.cur.execute(query, value)
            self.msg = True
            self.conn.commit()
        except Exception as e:
            print(e)
            self.msg = False
            self.conn.rollback()
        return self.msg

    def deleteStudent(self, student_id):
        try:
            query = "DELETE FROM Students where student_id = %s"
            value = [student_id]
            self.cur.execute(query, value)
            self.msg = True
            self.conn.commit()
        except Exception as e:
            print(e)
            self.msg = False
            self.conn.rollback()
        return self.msg

    def presentOfStudent(self, student_id, subject_id):
        try:
            query = "UPDATE attendance SET present = 'YES', absent = 'NO' where student_id = %s AND subject_id = %s"
            value = [student_id, subject_id]
            self.cur.execute(query, value)
            self.msg = True
            self.conn.commit()
        except Exception as e:
            print(e)
            self.msg = False
        return self.msg

    def absentOfStudent(self, student_id, subject_id):
        try:
            query = "UPDATE attendance SET present = 'NO', absent = 'YES' where student_id = %s AND subject_id = %s"
            value = [student_id, subject_id]
            self.cur.execute(query, value)
            self.msg = True
            self.conn.commit()
        except Exception as e:
            print(e)
            self.msg = False
        return self.msg

    # def holidayPresent(self, date, course_id):
    #     try:
    #         query = "UPDATE "
