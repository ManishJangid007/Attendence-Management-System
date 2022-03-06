from Connection import Connection


class InsertOperations():
    def __init__(self):
        self.obj = Connection()
        self.cur = self.obj.connect().cursor()
        self.con = self.obj.connect()
        self.msg = None

    def insertAdmin(self, user_name, password, status):
        try:
            query = "INSERT INTO Admins(user_name, password, status) VALUES(%s, %s, %s)"
            value = [user_name, password, status]
            self.cur.execute(query, value)
            self.con.commit()
            self.msg = True
        except Exception as e:
            print(e)
            self.msg = False
            self.con.rollback()
        return self.msg

    def insertTeacher(self, name, user_name, password, email="Null"):
        try:
            query = "INSERT INTO Teachers(name, email, user_name, password) values (%s, %s, %s, %s)"
            value = (name, email, user_name, password)
            self.cur.execute(query, value)
            self.con.commit()
            self.msg = True
        except Exception as e:
            print(e)
            self.con.rollback()
            self.msg = False
        return self.msg

    def insertCourses(self, name, course_duration):
        try:
            query = "INSERT INTO Courses(name, course_duration) values (%s, %s)"
            value = [name, course_duration]
            self.cur.execute(query, value)
            self.con.commit()
            self.msg = True
        except Exception as e:
            print(e)
            self.msg = False
            self.con.rollback()
        return self.msg

    def insertSubjects(self, name, year, course_id, teacher_id):
        try:
            query = "INSERT INTO Subjects(name, year, course_id, teacher_id) values (%s, %s, %s, %s)"
            value = [name, year, course_id, teacher_id]
            self.cur.execute(query, value)
            self.con.commit()
            self.msg = True
        except Exception as e:
            print(e)
            self.msg = False
            self.con.rollback()
        return self.msg

    def insertStudents(self, student_id, f_name, l_name, father_name, mother_name, gender, dob, age, phone_number, email, category, year, session, course_id, added_by):
        try:
            query = "INSERT INTO Students(student_id, f_name, l_name, father_name, mother_name, gender, dob, age, phone_number, email, category, year, session, course_id, added_by) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            value = [student_id, f_name, l_name, father_name, mother_name, gender, dob, age, phone_number, email, category, year, session, course_id, added_by]
            self.cur.execute(query, value)
            self.con.commit()
            self.msg = True
        except Exception as e:
            print(e)
            self.con.rollback()
            self.msg = False
        return self.msg

    def insertAttendance(self, course_id, year, teacher_id, subject_id):

        try:
            query = "INSERT INTO attendance(date, student_id, present, absent, year, subject_id, course_id, teacher_id) SELECT CURRENT_DATE, s.student_id, 'Null', 'Null', s.year, ss.subject_id, s.course_id, ss.teacher_id from Students s, Subjects ss WHERE s.course_id = %s AND s.year=%s AND ss.teacher_id = %s AND ss.subject_id = %s"
            value = [course_id, year, teacher_id, subject_id]
            self.cur.execute(query, value)
            self.con.commit()
            self.msg = True

        except Exception as e:
            print(e)
            self.con.rollback()
            self.msg = False

        return self.msg
