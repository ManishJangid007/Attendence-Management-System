from Connection import Connection


class SelectOperation():
    def __init__(self):
        try:
            obj = Connection()
            self.cur = obj.connect().cursor()
            self.con = obj.connect()
            self.data = None
            self.msg = ""
        except Exception as e:
            print(e)

    def showAdminTable(self):
        try:
            self.cur.execute("SELECT * FROM Admins")
            self.data = self.cur.fetchall()
            return self.data
        except Exception as e:
            print(e)

    def getTeacherProfile(self, teacher_id):
        try:
            query = "SELECT * FROM Teachers WHERE teacher_id = %s"
            value = [teacher_id]
            self.cur.execute(query, value)
            self.data = self.cur.fetchone()
            return self.data
        except Exception as e:
            print(e)

    def getTeacherBasicInfo(self):
        try:
            self.cur.execute("SELECT user_name, name, teacher_id FROM Teachers")
            self.data = self.cur.fetchall()
            self.data.pop(0)
            return self.data
        except Exception as e:
            print(e)

    def showCourseTable(self):
        try:
            self.cur.execute("SELECT * FROM Courses")
            self.data = self.cur.fetchall()
            return self.data
        except Exception as e:
            print(e)

    def getCourseCount(self):
        try:
            self.cur.execute("SELECT COUNT(*) FROM Courses")
            self.data = self.cur.fetchone()
            return self.data
        except Exception as e:
            print(e)

    def getCourseName(self, course_id):
        try:
            query = "SELECT name FROM Courses WHERE course_id = %s"
            value = [course_id]
            self.cur.execute(query, value)
            self.data = self.cur.fetchone()
            return self.data[0]
        except Exception as e:
            print(e)

    def showSubjectTable(self):
        try:
            self.cur.execute("SELECT * FROM Subjects")
            self.data = self.cur.fetchall()
            return self.data
        except Exception as e:
            print(e)

    def getSubjectCount(self, course_id):
        try:
            query = "SELECT COUNT(DISTINCT year) FROM subjects WHERE course_id = %s"
            value = [course_id]
            self.cur.execute(query, value)
            self.data = self.cur.fetchone()
            return self.data
        except Exception as e:
            print(e)

    def getStudentProfile(self, student_id):
        try:
            query = "SELECT * FROM Students WHERE student_id = %s"
            value = [student_id]
            self.cur.execute(query, value)
            self.data = self.cur.fetchone()
            return self.data
        except Exception as e:
            print(e)

    def getStudentBasicInfo(self):
        try:
            self.cur.execute("SELECT student_id, CONCAT(f_name,' ',l_name) AS Name FROM Students")
            self.data = self.cur.fetchall()
            return self.data
        except Exception as e:
            print(e)

    def getStudentName(self, student_id):
        try:
            query = "SELECT f_name, l_name from Students where student_id = %s"
            value = [student_id]
            self.cur.execute(query, value)
            data = self.cur.fetchone()
            name = data[0][0]+" "+data[0][1]
            return name
        except Exception as e:
            print(e)

    def showAttendanceTable(self):
        try:
            self.cur.execute("SELECT * FROM Attendance")
            self.data = self.cur.fetchall()
            return self.data
        except Exception as e:
            print(e)

    def getStudentId(self):
        try:
            self.cur.execute("SELECT student_id FROM Students")
            self.data = self.cur.fetchall()
            result = []
            for d in self.data:
                result.append(d)
            return result
        except Exception as e:
            print(e)

    def getCourseStudentId(self, course_id):
        try:
            query = "SELECT student_id FROM Students WHERE course_id = %s"
            value = [course_id]
            self.cur.execute(query, value)
            self.data = self.cur.fetchall()
            return self.data
        except Exception as e:
            print(e)

    def todayAttendance(self):
        def returnPresent(student_id):
            try:
                query = "SELECT * FROM attendance WHERE student_id = %s"
                value = [student_id]
                self.cur.execute(query, value)
                data = self.cur.fetchall()
                if len(data) > 0:
                    if data[len(data) - 1][2] == "YES":
                        return True
                    else:
                        return False
                else:
                    return False

            except Exception as e:
                print(e)
        data = []
        for i in range(1, int(''.join(map(str, self.getCourseCount())))+1):
            temp = []
            present = 0
            total_student = 0
            temp.append(self.getCourseName(i))
            for s_id in self.getCourseStudentId(i):
                total_student += 1
                if returnPresent(s_id[0]):
                    present += 1
            absent = total_student - present
            temp.append(present)
            temp.append(absent)
            temp.append(total_student)
            data.append(temp)

        data.pop(0)
        return data

    def yesterdayAttendance(self):
        def returnPresent(student_id):
            try:
                query = "SELECT * FROM attendance WHERE student_id = %s"
                value = [student_id]
                self.cur.execute(query, value)
                data = self.cur.fetchall()
                for id in data:
                    if id[2] == "YES":
                        return True
                    else:
                        pass
            except Exception as e:
                print(e)
        data = []
        for i in range(1, int(''.join(map(str, self.getCourseCount())))+1):
            temp = []
            present = 0
            total_student = 0
            temp.append(self.getCourseName(i))
            for s_id in self.getCourseStudentId(i):
                total_student += 1
                if returnPresent(s_id[0]):
                    present += 1
            absent = total_student - present
            temp.append(present)
            temp.append(absent)
            temp.append(total_student)
            data.append(temp)

        data.pop(0)
        return data

    def searchAttendance(self, date, course_id, year, subject_id):
        try:
            query = "SELECT student_id from Attendance where date =  %s AND course_id = %s AND year = %s AND subject_id = %s AND present = 'YES'"
            value = [date, course_id, year, subject_id]
            self.cur.execute(query, value)
            data = self.cur.fetchall()
            for i in range(0, len(data)):
                data[i] = list(data[i])
                data[i].append(self.getStudentName(data[i][0]))
            if data:
                return data
            else:
                try:
                    query = "SELECT aryaid from %s where course_id = %s AND year = %s AND subject_id = %s"
                    value = [date, course_id, year, subject_id]
                    self.cur.execute(query, value)
                    self.data = self.cur.fetchall()
                    return self.data
                except:
                    pass

            self.msg = "Record Not Found"
            return self.msg

        except Exception as e:
            print(e)


