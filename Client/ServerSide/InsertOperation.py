from ServerSide.Connection import Connection

class InsertOperation():
    def __init__(self):
        obj = Connection()
        self.conn = obj.connect()
        self.cur = self.conn.cursor()

    def insertAttendance(self, total_student, present_student, course_id, year, teacher_id, subject_id):
        try:
            for i in range(0, len(total_student)):
                present = False
                for j in range(0, len(present_student)):
                    if total_student[i][0] == present_student[j]:
                        query = "INSERT INTO Attendance(date, student_id, present, absent, year, subject_id, course_id, teacher_id) values(" \
                                "CURRENT_DATE, %s, 'Y', 'N', %s, %s, %s, %s)"
                        value = [present_student[j], year, subject_id, course_id, teacher_id]
                        self.cur.execute(query, value)
                        self.conn.commit()
                        present = True
                        break
                if not present:
                    query = "INSERT INTO Attendance(date, student_id, present, absent, year, subject_id, course_id, teacher_id) values(" \
                            "CURRENT_DATE, %s, 'N', 'Y', %s, %s, %s, %s)"
                    value = [total_student[i][0], year, subject_id, course_id, teacher_id]
                    self.cur.execute(query, value)
                    self.conn.commit()
            return True
        except:
            return False

    def setAbsentAll(self, total_student, course_id, year, teacher_id, subject_id):
        try:
            for i in total_student:
                query = "INSERT INTO Attendance(date, student_id, present, absent, year, subject_id, course_id, teacher_id) values(" \
                        "CURRENT_DATE, %s, 'N', 'Y', %s, %s, %s, %s)"
                value = [i[0], year, subject_id, course_id, teacher_id]
                self.cur.execute(query, value)
                self.conn.commit()
            return True
        except:
            return False
