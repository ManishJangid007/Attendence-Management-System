from Connection import Connection
from SelectOperation import SelectOperation
from EssentialFunction import EssentialFunction
from datetime import date


class UpdateOperation():
    def __init__(self):
        connect = Connection()
        self.get = SelectOperation()
        self.conn = connect.connect()
        self.cur = self.conn.cursor()
        self.data = []
        self.msg = None

    def updateAdminH(self, user_name, password):
        try:
            query = "UPDATE Admins set user_name = %s, password = %s WHERE admin_id = 1"
            value = [user_name, password]
            self.cur.execute(query, value)
            self.conn.commit()
            return True
        except:
            return False

    def blockAdmin(self, user_name):
        try:
            query = "UPDATE Admins set is_block = 'Y' WHERE user_name = %s"
            value = [user_name]
            self.cur.execute(query, value)
            self.conn.commit()
            return True
        except:
            return False

    def unBlockAdmin(self, user_name):
        try:
            query = "UPDATE Admins set is_block = 'N' WHERE user_name = %s"
            value = [user_name]
            self.cur.execute(query, value)
            self.conn.commit()
            return True
        except:
            return False

    def deleteAdmin(self, user_name):
        try:
            query = "SELECT status from Admins where user_name = %s"
            value = [user_name]
            self.cur.execute(query, value)
            self.data = self.cur.fetchone()
            if self.data[0].upper() == "H":
                self.msg = False
            else:
                query = "DELETE FROM Admins where user_name = %s"
                value = [user_name]
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
            query = "UPDATE Subjects set teacher_id = NULL WHERE teacher_id = %s"
            value = [teacher_id]
            self.cur.execute(query, value)
            self.conn.commit()
            query = "UPDATE Attendance set teacher_id = NULL WHERE teacher_id = %s"
            self.cur.execute(query, value)
            self.conn.commit()
            query = "DELETE FROM Teachers where teacher_id = %s"
            self.cur.execute(query, value)
            self.msg = True
            self.conn.commit()
        except Exception as e:
            print(e)
            self.msg = False
            self.conn.rollback()
        return self.msg

    def updateTeacher(self, teacher_id, name, email, phone_no):
        try:
            query = "UPDATE Teachers SET name = %s, email = %s, phone_no = %s WHERE teacher_id = %s"
            value = [name, email, phone_no, teacher_id]
            self.cur.execute(query, value)
            self.conn.commit()
            self.msg = True
        except:
            self.msg = False
        return self.msg

    def assignTeacher(self, course_name, year, subject_name, teacher_id):
        try:
            course_id = SelectOperation().getCourseId(course_name)
            subject_id = SelectOperation().getSubject_id(subject_name, course_id, year)
            query = "UPDATE Subjects set teacher_id = %s WHERE subject_id = %s"
            value = [teacher_id, subject_id]
            self.cur.execute(query, value)
            self.conn.commit()
            return True
        except:
            return False

    def deleteCourse(self, course_id):
        try:
            query = "DELETE FROM Subjects WHERE course_id = %s"
            value = [course_id]
            self.cur.execute(query, value)
            self.conn.commit()
            query = "UPDATE Attendance SET subject_id = NULL, course_id = NULL WHERE course_id = %s"
            self.cur.execute(query, value)
            self.conn.commit()
            query = "UPDATE Students set course_id = NULL WHERE course_id = %s"
            self.cur.execute(query, value)
            self.conn.commit()
            query = "DELETE FROM Courses where course_id = %s"
            self.cur.execute(query, value)
            self.msg = True
            self.conn.commit()
        except Exception as e:
            print(e)
            self.msg = False
            self.conn.rollback()
        return self.msg

    def deleteSubject(self, course_name, course_year, subject_name):
        try:
            course_id = SelectOperation().getCourseId(course_name)
            subject_id = SelectOperation().getSubject_id(subject_name, course_id, course_year)
            query = "UPDATE Attendance set subject_id = NULL WHERE subject_id = %s"
            value = [subject_id]
            self.cur.execute(query, value)
            self.conn.commit()
            query = "DELETE FROM Subjects where subject_id = %s"
            self.cur.execute(query, value)
            self.msg = True
            self.conn.commit()
        except:
            self.msg = False
            self.conn.rollback()
        return self.msg

    def removeTeacherFromSubject(self, subject_id):
        try:
            query = "UPDATE Subjects set teacher_id = NULL WHERE subject_id = %s"
            value = [subject_id]
            self.cur.execute(query, value)
            self.conn.commit()
            self.msg = True
        except:
            self.msg = False

        return self.msg

    def deleteStudent(self, student_id):
        try:
            query = "DELETE FROM Attendance WHERE student_id = %s"
            value = [student_id]
            self.cur.execute(query, value)
            self.conn.commit()
            query = "DELETE FROM Students where student_id = %s"
            self.cur.execute(query, value)
            self.msg = True
            self.conn.commit()
        except:
            self.msg = False
            self.conn.rollback()
        return self.msg

    def updateStudent(self, student_id, f_name, l_name, father_name, mother_name, gender, dob, phone_number, email, year, course_name):
        try:
            course_id = SelectOperation().getCourseId(course_name)
            cd = int(SelectOperation().getCourseDuration(course_name))
            current_year = date.today().year
            graduation_year = int(current_year) + (cd - int(year)) + 1
            session = f"{current_year} - {graduation_year}"
            query = "UPDATE Students set f_name = %s, l_name = %s, father_name = %s, mother_name = %s, gender = %s, dob = %s, phone_number = %s, email = %s, year = %s, session = %s, course_id = %s WHERE student_id = %s"
            value = [f_name, l_name, father_name, mother_name, gender, dob, phone_number, email, year, session, course_id, student_id]
            self.cur.execute(query, value)
            self.conn.commit()
            EssentialFunction().updateAge(dob, student_id)
            self.msg = True
        except Exception as e:
            print(e)
            self.conn.rollback()
            self.msg = False
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
