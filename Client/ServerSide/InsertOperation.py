from ServerSide.Connection import Connection

class InsertOperation():
    def __init__(self):
        obj = Connection()
        self.conn = obj.connect()
        self.cur = self.conn.cursor()

    def insertAttendance(self, total_student, present_student, course_id, year, teacher_id, subject_id):
        try:
            for i in range(0, len(total_student)):
                for i in range(0, len(present_student)):
                    print(present_student)


            # query = "INSERT INTO attendance(date, student_id, present, absent, year, subject_id, course_id, teacher_id) SELECT CURRENT_DATE, s.student_id, 'Null', 'Null', s.year, ss.subject_id, s.course_id, ss.teacher_id from Students s, Subjects ss WHERE s.course_id = %s AND s.year=%s AND ss.teacher_id = %s AND ss.subject_id = %s"
            # value = [course_id, year, teacher_id, subject_id]
            # self.cur.execute(query, value)
            # self.con.commit()
            # self.msg = True

        except Exception as e:
            print(e)