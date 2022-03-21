from ServerSide.SelectOperation import SelectOperation
from ServerSide.InsertOperation import InsertOperation

select = SelectOperation()
# print(select.verifyTeacher('S', 's'))
# print(select.getSubjectAccordingToTeacher("s"))
print(select.getStudentAccordingToYear(2, "1"))
# print(select.checkSubjectAttendance("21-03-2022", 22))

insert = InsertOperation()
# insert.insertAttendance(select.getStudentAccordingToYear(2, "1"), 4, 5, 5, 5, 5)
