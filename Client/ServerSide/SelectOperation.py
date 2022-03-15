from ServerSide.Connection import Connection


class SelectOperation():
    def __init__(self):
        obj = Connection()
        self.conn = obj.connect()
        self.cur = self.conn.cursor()

    def verifyTeacher(self, user_name, password):
        try:
            query = "SELECT * FROM Teachers WHERE user_name = %s AND password = %s"
            value = [user_name, password]
            self.cur.execute(query, value)
            result = self.cur.fetchone()
            if result:
                return True
            else:
                return False
        except:
            pass

    def getTeacherId(self, t_user_name):
        try:
            query = "SELECT teacher_id FROM Teachers WHERE user_name = %s"
            value = [t_user_name]
            self.cur.execute(query, value)
            result = self.cur.fetchone()
            return result[0]
        except:
            pass

    def getSubjectAccordingToTeacher(self, t_user_name):
        try:
            #subject name course_name year
            teacher_id = self.getTeacherId(t_user_name)
            query = "SELECT subject_id, course_id, year FROM Subjects WHERE teacher_id = %s"
            value = [teacher_id]
            self.cur.execute(query, value)
            result = self.cur.fetchall()
            data = []
            for i in range(0, len(result)):
                temp = []
                temp.append(self.getSubjectName(result[i][0]))
                temp.append(self.getCourseName(result[i][1]))
                temp.append(result[i][2])
                temp.append(result[i][0])
                temp.append(result[i][1])
                data.append(temp)
            return data
        except:
            pass

    def getCourseName(self, course_id):  # return course name
        try:
            query = "SELECT name FROM Courses WHERE course_id = %s"
            value = [course_id]
            self.cur.execute(query, value)
            data = self.cur.fetchone()
            return data[0]
        except:
            pass

    def getSubjectName(self, subject_id):  # return subject name
        try:
            query = "SELECT name FROM Subjects WHERE subject_id = %s"
            value = [subject_id]
            self.cur.execute(query, value)
            data = self.cur.fetchone()
            return data[0]
        except:
            pass