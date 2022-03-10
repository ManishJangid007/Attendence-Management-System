
from ServerSide.Connection import Connection
from ServerSide.SelectOperation import SelectOperation


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

    def duplicateSubject(self, course_name, year, subject_name):
        try:
            course_id = SelectOperation().getCourseId(course_name)
            query = "SELECT * FROM Subjects WHERE name = %s AND year = %s AND course_id = %s"
            value = [subject_name, year, course_id]
            self.cur.execute(query, value)
            data = self.cur.fetchone()
            if data:
                return True
            else:
                return False
        except:
            return False

