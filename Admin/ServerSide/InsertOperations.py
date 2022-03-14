from ServerSide.EssentialFunction import EssentialFunction
from  datetime import date
from ServerSide.SelectOperation import SelectOperation
from ServerSide.Connection import Connection

class InsertOperations():
    def __init__(self):
        self.obj = Connection()
        self.cur = self.obj.connect().cursor()
        self.con = self.obj.connect()
        self.msg = None

    def insertAdmin(self, user_name, password, status='M', is_block='N'):
        try:
            query = "INSERT INTO Admins(user_name, password, status, is_block) VALUES(%s, %s, %s, %s)"
            value = [user_name, password, status, is_block]
            self.cur.execute(query, value)
            self.con.commit()
            self.msg = True
        except:
            self.msg = False
            self.con.rollback()
        return self.msg

    def insertTeacher(self, name, user_name, password, phone_no, email="Null"):
        try:
            query = "INSERT INTO Teachers(name, phone_no, email, user_name, password) values (%s, %s, %s, %s, %s)"
            value = (name, phone_no, email, user_name, password)
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

    def insertSubjects(self, subject_name, year, course_name):
        try:
            course_id = SelectOperation().getCourseId(course_name)
            query = "INSERT INTO Subjects(name, year, course_id, teacher_id) values (%s, %s, %s, NULL)"
            value = [subject_name, year, course_id]
            self.cur.execute(query, value)
            self.con.commit()
            self.msg = True
        except Exception as e:
            print(e)
            self.msg = False
            self.con.rollback()
        return self.msg

    def insertStudents(self, student_id, f_name, l_name, father_name, mother_name, gender, dob, phone_number, email, year, course_name, added_by):
        try:
            course_id = SelectOperation().getCourseId(course_name)
            cd = int(SelectOperation().getCourseDuration(course_name))
            current_year = date.today().year
            graduation_year = int(current_year) + (cd-int(year)) + 1
            session = f"{current_year} - {graduation_year}"
            query = "INSERT INTO Students(student_id, f_name, l_name, father_name, mother_name, gender, dob, phone_number, email, year, session, course_id, added_by) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            value = [student_id, f_name, l_name, father_name, mother_name, gender, dob, phone_number, email, year, session, course_id, added_by]
            self.cur.execute(query, value)
            self.con.commit()
            EssentialFunction().updateAge(dob, student_id)
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
