from ServerSide.Connection import Connection

class InitialSetup():
    def __init__(self):
        obj = Connection()
        self.con = obj.setupConnection()
        self.cur = obj.setupConnection().cursor()

    def setup(self):
        try:
            # creating tables.......

            self.cur.execute(
                "CREATE DATABASE amsx505")
            self.cur.execute(
                "USE amsx505")
            self.cur.execute(
                "CREATE TABLE Admins(admin_id int AUTO_INCREMENT PRIMARY KEY, user_name varchar(255), password varchar(255), status varchar(255), is_block varchar(255))")
            self.cur.execute(
                "CREATE TABLE Teachers(teacher_id int AUTO_INCREMENT PRIMARY KEY, name varchar(255),phone_no varchar(50), email varchar(255), user_name varchar(255), password varchar(255))")
            self.cur.execute(
                "CREATE TABLE Courses(course_id int AUTO_INCREMENT PRIMARY KEY, name varchar(255), course_duration int(50))")
            self.cur.execute(
                "CREATE TABLE Subjects(subject_id int AUTO_INCREMENT PRIMARY KEY, name varchar(255), year varchar(100), course_id int(50), teacher_id int(50), FOREIGN KEY (course_id) REFERENCES Courses(course_id), FOREIGN KEY (teacher_id) REFERENCES Teachers(teacher_id))")
            self.cur.execute(
                "CREATE TABLE Students(student_id varchar(255) NOT NULL PRIMARY KEY, f_name varchar(255), l_name varchar(255), father_name varchar(255), mother_name varchar(255), gender varchar(255), dob varchar(255), age int(20), phone_number varchar(255), email varchar(255), year varchar(100), session varchar(100), course_id int(50), added_by varchar(255),FOREIGN KEY(course_id) REFERENCES Courses(course_id))")
            self.cur.execute(
                "CREATE TABLE Attendance(date varchar(255), student_id varchar(255), present varchar(10), absent varchar(10), year varchar(255), subject_id int(50), course_id int(50), teacher_id int(50), FOREIGN KEY(student_id) REFERENCES Students(student_id), FOREIGN KEY(subject_id) REFERENCES Subjects(subject_id), FOREIGN KEY(course_id) REFERENCES Courses(course_id), FOREIGN KEY(teacher_id) REFERENCES Teachers(teacher_id))")
            self.cur.execute(
                "CREATE TABLE Holiday_Weekly(day varchar(255) NOT NULL PRIMARY KEY)")
            self.cur.execute(
                "CREATE TABLE Holiday_Occasionally(holiday_id int AUTO_INCREMENT PRIMARY KEY, occasion varchar(255), holiday_from varchar(255), holiday_to varchar(255))")
            self.cur.execute(
                "CREATE DATABASE backupamsx505")

            self.initialRecords()

            return True
        except:
            return False

    def initialRecords(self):
        self.cur.execute(
            "INSERT INTO Admins(user_name, password, status) VALUES ('admin@root', 'admin@123', 'H')")
        self.cur.execute(
            "INSERT INTO Teachers(name, email, user_name, password) VALUES ('ALL', 'aicte@gmail.com', 'aryabhatta@ajmer', '12345')")
        self.cur.execute(
            "INSERT INTO Courses(name, course_duration) values ('ALL', 0)")
        self.cur.execute(
            "INSERT INTO Subjects(name, year, course_id, teacher_id) values ('ALL', 0, 1, 1)")
        self.con.commit()
