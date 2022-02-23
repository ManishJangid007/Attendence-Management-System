from Connection import Connection


class SelectOperation():
    def __init__(self):
        try:
            obj = Connection()
            self.cur = obj.connect().cursor()
            self.con = obj.connect()
            self.data = None
        except Exception as e:
            print(e)

    def showAdminTable(self):
        try:
            self.cur.execute("SELECT * FROM Admins")
            self.data = self.cur.fetchall()
            return self.data
        except Exception as e:
            print(e)

    def showTeacherTable(self):
        try:
            self.cur.execute("SELECT * FROM Teachers")
            self.data = self.cur.fetchall()
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

    def showStudentTable(self):
        try:
            self.cur.execute("SELECT * FROM Students")
            self.data = self.cur.fetchall()
            return self.data
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

    def getCourseStudentId(self, course_id, year):
        try:
            query = "SELECT student_id FROM Students WHERE course_id = %s AND year = %s"
            value = [course_id, year]
            self.cur.execute(query, value)
            self.data = self.cur.fetchall()
            return self.data
        except Exception as e:
            print(e)

    def currentAttendance(self):
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

        for i in range(1, int(''.join(map(str, self.getCourseCount())))+1):
            for j in range(1, int(''.join(map(str, self.getSubjectCount(i))))+1):
                # print(i, "\t", j)
                count = 0
                total_student = 0
                for s_id in self.getCourseStudentId(i, j):
                    total_student += 1
                    if returnPresent(s_id[0]):
                        count += 1
                print(count, total_student)

        return count, total_student

    # def yesterdayReportData(self, date):
    #     result = []
    #
    #     def courseAttendance(student_id, course_id, year):
    #         try:
    #             query = "SELECT present from Attendance where student_id=%s AND course_id = %s AND year = %s"
    #             value = [student_id, course_id, year]
    #             self.cur.execute(query, value)
    #             temp = self.cur.fetchall()
    #             print(temp[0])
    #             if temp[len(temp)-1] == "NO":
    #                 print("Good")
    #                 return True
    #             else:
    #                 return False
    #         except Exception as e:
    #             print(e)
    #
    #     p_count = 0
    #     a_count = 0
    #     for id in self.getCourseStudentId(2, "3"):
    #         if courseAttendance(id[0], 2, "3"):
    #             p_count += 1
    #         else:
    #             a_count += 1
    #     print(p_count, "\n", a_count)
    # try:
    #     self.cur.execute("SELECT course_id FROM courses")
    #     data = self.cur.fetchall()
    #     print(data)
    # except Exception as e:
    #     print(e)
