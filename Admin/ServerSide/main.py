from Connection import Connection
from InitialSetup import InitialSetup
from InsertOperations import InsertOperations
from SelectOperation import SelectOperation
from UpdateOperation import UpdateOperation
from RawData import RawData
from EssentialFunction import EssentialFunction
from DuplicateVerification import DuplicateVerification

obj = Connection()
conn = obj.connect()
cur = conn.cursor()

# cur.execute("SHOW TABLES")
# data = cur.fetchall()
# for i in range(0, len(data)):
#     print(data[i][0])

run = InitialSetup()
# if run.setup():
#     print("Database is created successful")
# else:
#     print("While creating database there is problem")

raw = RawData()
insert = InsertOperations()
# if insert.insertAdmin("admin@aryabhatta", "12345", "high"):
#     print("Admin record inserted successful")
# else:
#     print("Admin record doesn't insert")

# for i in raw.teacher_data:
#     if insert.insertTeacher(i[0], i[1], i[2], i[3]):
#         print("Teacher record inserted successful")
#     else:
#         print("Teacher record doesn't insert")

# for i in raw.course_data:
#     if insert.insertCourses(i[0], i[1]):
#         print("Course record inserted successful")
#     else:
#         print("Course record doesn't inserted")

# for i in raw.subject_data:
#     if insert.insertSubjects(i[0], i[1], i[2], i[3]):
#         print("Subject record inserted successful")
#     else:
#         print("Subject record doesn't inserted")

# for i in raw.student_data:
#     if insert.insertStudents(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11]):
#         print("Students record inserted successful")
#     else:
#         print("Students record doesn't inserted")

# if insert.insertAttendance(6, "1", 7, 16):
#     print("Attendance record inserted successful")
# else:
#     print("Attendance record doesn't inserted")

# print(insert.insertSubjects("DBMS", "2", "BCAA"))
select = SelectOperation()
# print(select.getSubjectAccordingToYear("BCA", "1"))
# print(select.checkExistenceOfAdmin("leeena"))
# print(select.isPriorityHigh("admin@aryabhatta"))
# print(select.showAdmins())
# print(select.getStudentProfile("aryaid101"))
# print(select.getStudentBasicInfo("BCA", "1"))
# print(select.totalPresentCount("aryaid502"))
# # data = select.showAdminTable()
# # for x in data:
# #     print("%d %s %s" % (x[0], x[1], x[2]))

# print(select.getStudentProfile("aryaid301"))

# print(select.getTeacherAccordingToCourse("2", "MCA"))
# print("Today's report")
# print(select.todayAttendanceReport())
# print(select.getTotalStudentCount())
# print(select.todayTotalPresentReport())
# print(select.yesterdayAttendance())
# print(select.checkSubjectAttendance("22-03-2022", 10))
# print(select.searchAttendance("22-03-2022", "MCA", "1", "Computer Architecture"))

# data = select.getStudentBasicInfo()
# print(data)

# data = select.getTeacherBasicInfo()
# print(select.getTeacherProfile(100))

# for i in data:
#     print(select.getTeacherProfile(i[2]))
# select.yesterdayReportData("ggh")

# print(select.verifyAdmin("admin@aryabhatta", "12345"))

# print(select.getTeacherSubjects(13))

update = UpdateOperation()
# print(update.updateAdminUserName("b", "f"))
# print(update.deleteAdmin("admin@aryabhatta"))
# print(update.blockAdmin("leena"))
# print(update.updateStudent("aryaid101", "Ram", "Sharma", 'xyz', 'abc', 'male', '22-07-1995',  'xxxxxxxxxx', 'fhg@gmail.com', '1', "BCA"))
# print(update.deleteStudent("aryaid302"))
# print(update.deleteSubject("BCA", "3", "C++"))
# update.deleteCourse(8)
# print(update.assignTeacher("BCA", "1", "C++", 14))
# if update.deleteAdmin(1):
#     print("Admin is deleted")
# else:
#     print("Admin can't be deleted")

# if update.absentOfStudent("aryaid502", 16):
#     print("updated attendance")
# else:
#     print("update doesn't performed")
#
# if update.presentOfStudent("aryaid501", 16):
#     print("updated attendance")
# else:
#     print("update doesn't performed")


# if update.deleteStudent("aryaid201"):
#     print("deleted")
# else:
#     print("Doesn't deleted")


# def createTable(name):
#     try:
#         query = "CREATE TABLE %s(roll_no int(50))"
#         value = [name]
#         cur.execute(query, value)
#     except Exception as e:
#         print(e)
#
# createTable("Google")

# update.deleteTeacher(7)
es = EssentialFunction()
# if es.backupAttendance():
#     print("Backup Table is created Successfully")
# else:
#     print("Table isn't created")
# print(es.updateAge("22-07-2002", "aryaid101"))

dv = DuplicateVerification()
# print(dv.duplicateTeacher("xyz@gmaiasdal.com"))
# print(dv.duplicateCourse("BCA"))
# print(dv.duplicateSubject("BCA", "2", "c++"))
# print(dv.duplicateStudent_id("aryaid109"))
