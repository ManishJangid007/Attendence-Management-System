from Connection import Connection
from InitialSetup import InitialSetup
from InsertOperations import InsertOperations
from SelectOperation import SelectOperation
from UpdateOperation import UpdateOperation
from RawData import RawData

obj = Connection()
cur = obj.setupConnection().cursor()
con = obj.setupConnection()

# run = InitialSetup()
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
#
# for i in raw.teacher_data:
#     if insert.insertTeacher(i[0], i[1], i[2], i[3]):
#         print("Teacher record inserted successful")
#     else:
#         print("Teacher record doesn't insert")
#
# for i in raw.course_data:
#     if insert.insertCourses(i[0]):
#         print("Course record inserted successful")
#     else:
#         print("Course record doesn't inserted")
#
# for i in raw.subject_data:
#     if insert.insertSubjects(i[0], i[1], i[2], i[3]):
#         print("Subject record inserted successful")
#     else:
#         print("Subject record doesn't inserted")
#
# for i in raw.student_data:
#     if insert.insertStudents(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12], i[13], i[14]):
#         print("Students record inserted successful")
#     else:
#         print("Students record doesn't inserted")

# if insert.insertAttendance(3, "1", 8, 10):
#     print("Attendance record inserted successful")
# else:
#     print("Attendance record doesn't inserted")

select = SelectOperation()
# # data = select.showAdminTable()
# # for x in data:
# #     print("%d %s %s" % (x[0], x[1], x[2]))
#
# data = select.getStudentId()
# for x in data:
#     print(x)

data = select.getStudentId()
a, d = select.currentAttendance()
print(a)
print(d)

# select.yesterdayReportData("ggh")
update = UpdateOperation()
# if update.absentOfStudent("aryaid202", 10):
#     print("updated attendance")
# else:
#     print("update doesn't performed")
#
# if update.presentOfStudent("aryaid202", 10):
#     print("updated attendance")
# else:
#     print("update doesn't performed")


# if update.deleteStudent("aryaid201"):
#     print("deleted")
# else:
#     print("Doesn't deleted")