from ServerSide.Connection import Connection
from datetime import date, timedelta


class SelectOperation():
    def __init__(self):
        try:
            obj = Connection()
            self.cur = obj.connect().cursor()
            self.con = obj.connect()
            self.data = []
            self.msg = ""
        except Exception as e:
            print(e)

    def showAdmins(self):
        try:
            self.cur.execute("SELECT * FROM Admins")
            self.data = self.cur.fetchall()
            return self.data
        except Exception as e:
            print(e)

    def verifyAdmin(self, username, password):
        try:
            query = "SELECT * FROM Admins where user_name = %s AND password = %s"
            value = [username, password]
            self.cur.execute(query, value)
            data = self.cur.fetchone()
            if data:
                if data[1] == username and data[2] == password:
                    return True
                else:
                    return False
            else:
                return False
        except Exception as e:
            print(e)

    def checkExistenceOfAdmin(self, user_name):
        try:
            query = "SELECT user_name FROM admins WHERE user_name = %s"
            value = [user_name]
            self.cur.execute(query, value)
            self.data = self.cur.fetchone()
            if self.data:
                return True
            else:
                return False
        except:
            pass

    def isBlocked(self, user_name):
        try:
            query = "SELECT is_Block FROM admins WHERE user_name = %s"
            value = [user_name]
            self.cur.execute(query, value)
            self.data = self.cur.fetchone()
            if self.data[0] == 'Y' or self.data[0] == 'y':
                return True
            else:
                return False
        except:
            pass

    def isPriorityHigh(self, user_name):
        try:
            query = "SELECT status FROM admins WHERE user_name =  %s"
            value = [user_name]
            self.cur.execute(query, value)
            self.data = self.cur.fetchone()
            if self.data[0].upper() == "H":
                return True
            else:
                return False
        except:
            pass

    def getTeacherProfile(self, teacher_id):
        try:
            query = "SELECT name, email, phone_no  FROM Teachers WHERE teacher_id = %s"
            value = [teacher_id]
            self.cur.execute(query, value)
            self.data = self.cur.fetchone()
            return self.data
        except:
            return self.data

    def getTeacherBasicInfo(self):
        try:
            self.cur.execute("SELECT user_name, name, teacher_id FROM Teachers")
            self.data = self.cur.fetchall()
            self.data.pop(0)
            return self.data
        except Exception as e:
            print(e)

    def getTeacherName(self, id):
        try:
            query = "SELECT name FROM Teachers WHERE teacher_id = %s"
            value = [id]
            self.cur.execute(query, value)
            self.data = self.cur.fetchone()
            return self.data[0]
        except:
            pass

    def getTeacherNameWithUserName(self, user_name):
        try:
            query = "SELECT name FROM Teachers WHERE user_name = %s"
            value = [user_name]
            self.cur.execute(query, value)
            self.data = self.cur.fetchone()
            return self.data[0]
        except:
            pass

    def getTeacherSubjects(self, teacher_id):
        try:
            query = "SELECT subject_id, name , course_id, year FROM Subjects WHERE teacher_id = %s"
            value = [teacher_id]
            self.cur.execute(query, value)
            self.data = self.cur.fetchall()
            print(type(self.data))
            result = []
            for i in self.data:
                temp = list(i)
                temp[0] = i[0]
                temp[1] = i[1]
                temp[2] = self.getCourseName(i[2])
                temp[3] = i[3]
                result.append(temp)
            return result
        except:
            pass

    def getTeacherAccordingToCourse(self, year, course_name):
        try:
            course_id = self.getCourseId(course_name)
            query = "SELECT name, teacher_id FROM Subjects WHERE year = %s AND course_id = %s"
            value = [year, course_id]
            self.cur.execute(query, value)
            data = self.cur.fetchall()
            for i in range(0, len(data)):
                teacher_name = self.getTeacherName(data[i][1])
                if teacher_name is None:
                    teacher_name = 'Not Assigned'
                data[i] = list(data[i])
                data[i].pop(1)
                data[i].append(teacher_name)
            return data
        except:
            pass

    def getCourse(self):  # return course_name and course Duration
        try:
            self.cur.execute("SELECT name, course_duration, course_id FROM Courses")
            self.data = self.cur.fetchall()
            self.data.pop(0)
            return self.data
        except Exception as e:
            print(e)

    def getCourseCount(self):  # return course count
        try:
            self.cur.execute("SELECT COUNT(*) FROM Courses")
            self.data = self.cur.fetchone()
            return self.data
        except Exception as e:
            print(e)

    def getCourseName(self, course_id):  # return course name
        try:
            query = "SELECT name FROM Courses WHERE course_id = %s"
            value = [course_id]
            self.cur.execute(query, value)
            self.data = self.cur.fetchone()
            return self.data[0]
        except Exception as e:
            print(e)

    def getCourseId(self, course_name):  # return course id
        try:
            query = "SELECT course_id FROM Courses WHERE name = %s"
            value = [course_name]
            self.cur.execute(query, value)
            self.data = self.cur.fetchone()
            return self.data[0]
        except Exception as e:
            print(e)
            return self.data

    def checkExistenceCourse(self, course_name):  # check course Exist or not
        try:
            query = "SELECT * FROM Courses WHERE name = %s"
            value = [course_name]
            self.cur.execute(query, value)
            self.data = self.cur.fetchone()
            if self.data:
                return True
            else:
                return False
        except:
            return False

    def getCourseDuration(self, course_name):  # get Specific course Duration
        try:
            query = "SELECT course_duration FROM Courses WHERE name = %s"
            value = [course_name]
            self.cur.execute(query, value)
            self.data = self.cur.fetchone()
            return self.data[0]
        except:
            return self.data

    def showSubjectTable(self):
        try:
            self.cur.execute("SELECT * FROM Subjects")
            self.data = self.cur.fetchall()
            return self.data
        except Exception as e:
            print(e)

    def getSubjectName(self, subject_id):  # return subject name
        try:
            query = "SELECT name FROM Subjects WHERE subject_id = %s"
            value = [subject_id]
            self.cur.execute(query, value)
            self.data = self.cur.fetchone()
            return self.data[0]
        except Exception as e:
            print(e)

    def getSubjectCount(self, course_id):  # return subject count
        try:
            query = "SELECT COUNT(DISTINCT year) FROM subjects WHERE course_id = %s"
            value = [course_id]
            self.cur.execute(query, value)
            self.data = self.cur.fetchone()
            return self.data
        except Exception as e:
            print(e)

    def getSubject_id(self, subject_name, course_id, year):
        try:
            query = "SELECT Subject_id FROM Subjects WHERE name = %s AND year = %s AND course_id = %s"
            value = [subject_name, year, course_id]
            self.cur.execute(query, value)
            self.data = self.cur.fetchone()
            return self.data[0]
        except:
            pass

    def getSubjectId(self, course_id):
        try:
            query = "SELECT subject_Id from Subjects WHERE course_id = %s"
            value = [course_id]
            self.cur.execute(query, value)
            self.data = self.cur.fetchall()
            return self.data
        except:
            pass

    def getSubjectAccordingToYear(self, course_name, year):
        try:
            course_id = self.getCourseId(course_name)
            query = "SELECT name From Subjects WHERE course_id = %s AND year = %s"
            value = [course_id, year]
            self.cur.execute(query, value)
            self.data = self.cur.fetchall()
            return self.data
        except:
            pass


    def getStudentProfile(self, student_id):   # return Student Profile

        try:
            query = "SELECT * FROM Students WHERE student_id = %s"
            value = [student_id]
            self.cur.execute(query, value)
            self.data = self.cur.fetchone()
            return self.data
        except Exception as e:
            print(e)

    def getStudentBasicInfo(self, course_name, year):
        try:
            course_id = SelectOperation().getCourseId(course_name)
            query = "SELECT student_id, f_name, l_name FROM Students WHERE course_id = %s AND year = %s"
            value = [course_id, year]
            self.cur.execute(query, value)
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
            name = data[0] + " " + data[1]
            return name
        except:
            pass

    def getTotalStudentCount(self):
        try:
            self.cur.execute("SELECT count(*) FROM Students")
            self.data = self.cur.fetchone()
            return self.data[0]
        except:
            pass


    def showAttendanceTable(self):
        try:
            self.cur.execute("SELECT * FROM Attendance")
            self.data = self.cur.fetchall()
            return self.data
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

    def todayTotalPresentReport(self):
        try:
            self.cur.execute("SELECT COUNT(*) FROM Attendance WHERE present = 'Y'")
            self.data = self.cur.fetchone()
            return self.data[0]
        except:
            pass

    def todayAttendanceReport(self):
        def returnPresent(student_id, subject_id):
            try:
                query = "SELECT * FROM attendance WHERE student_id = %s AND subject_id = %s"
                value = [student_id, subject_id]
                self.cur.execute(query, value)
                data = self.cur.fetchall()
                if len(data) > 0:
                    if data[len(data) - 1][2] == "Y":
                        return True
                    else:
                        return False
                else:
                    return False

            except:
                pass

        data = []
        for i in self.getCourse():
            temp = []
            present = 0
            total_student = 0
            temp.append(self.getCourseName(i[2]))
            for s_id in self.getCourseStudentId(i[2]):
                total_student += 1
                for subject in self.getSubjectId(i[2]):
                    if returnPresent(s_id[0], subject[0]):
                        present += 1
            absent = total_student - present
            temp.append(present)
            temp.append(absent)
            temp.append(total_student)
            data.append(temp)

        return data

    def yesterdayAttendance(self):  # return Previous Day Attendance
        def returnPresent(student_id):
            try:
                query = "SELECT * FROM attendance WHERE student_id = %s AND date = DATE_SUB(CURDATE(), INTERVAL 1 DAY)"
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
        for i in range(1, int(''.join(map(str, self.getCourseCount()))) + 1):
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

    def searchAttendance(self, date, course_id, year,
                         subject_id):  # return present of search Student of a particular date
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
                    delete = '-'
                    for c in delete:
                        date = date.replace(c, '')
                    date = 'd' + date
                    query = "SELECT student_id from backupamsx505.{date} where course_id = %s AND year = %s AND subject_id = %s AND present = 'YES'".format(
                        date=date)
                    value = [course_id, year, subject_id]
                    self.cur.execute(query, value)
                    data = self.cur.fetchall()
                    for i in range(0, len(data)):
                        data[i] = list(data[i])
                        data[i].append(self.getStudentName(data[i][0]))
                    if data:
                        return data
                    else:
                        self.msg = "Record Not Found"
                        return self.msg
                except:
                    pass

        except Exception as e:
            print(e)

    def totalPresentCount(self, student_id):  # return total count of student of a year
        try:
            record = []
            query = "SELECT course_id FROM Students WHERE student_id = %s"
            value = [student_id]
            self.cur.execute(query, value)
            temp = self.cur.fetchone()
            course_id = temp[0]
            query = "SELECT year FROM Students WHERE student_id = %s"
            value = [student_id]
            self.cur.execute(query, value)
            temp = self.cur.fetchone()
            year = temp[0]
            query = "SELECT subject_id FROM Subjects WHERE course_id = %s AND year = %s"
            value = [course_id, year]
            self.cur.execute(query, value)
            subject_id = self.cur.fetchall()

            def daterange(start_date, end_date):
                for n in range(int((end_date - start_date).days)):
                    yield start_date + timedelta(n)

            start_date = date(date.today().year - 1, 6, 1)
            end_date = date.today()
            self.cur.execute("USE backupamsx505")
            self.cur.execute("SHOW TABLES")
            result = self.cur.fetchall()
            for subject in subject_id:
                self.cur.execute("USE amsx505")
                total_present = 0
                row = []
                row.append(self.getSubjectName(subject[0]))
                for single_date in daterange(start_date, end_date):
                    day = single_date.strftime("%Y-%m-%d")
                    query = "SELECT present FROM Attendance WHERE student_id = %s AND date = %s AND course_id =  %s AND subject_id = %s AND year = %s"
                    value = [student_id, day, course_id, subject[0], year]
                    self.cur.execute(query, value)
                    self.data = self.cur.fetchone()
                    if self.data:
                        if self.data[0].upper() == "YES":
                            total_present += 1
                    else:
                        try:
                            delete = '-'
                            for c in delete:
                                day = day.replace(c, '')
                            day = 'd' + day
                            for i in range(0, len(result)):
                                if result[i][0] == day:
                                    query = "SElECT present FROM backupamsx505.{day} WHERE student_id = %s AND course_id =  %s AND subject_id = %s AND year = %s".format(
                                        day=day)
                                    value = [student_id, course_id, subject[0], year]
                                    self.cur.execute(query, value)
                                    data = self.cur.fetchone()
                                    if data:
                                        if data[0].upper() == "YES":
                                            total_present += 1
                                            break
                        except Exception as e:
                            print(e)

                row.append(total_present)
                record.append(row)

            return record
        except Exception as e:
            print(e)
