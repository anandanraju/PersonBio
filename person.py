class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    def PersonInfo(self):
        print('Name : {}'.format(self.name))
        print('Age : {}'.format(self.age))
        print('Gender : {}'.format(self.gender))
    

class Student(Person):
    def __init__(self,name,age,gender,studentid,fees):
        Person.__init__(self,name,age,gender)
        self.studentid = studentid
        self.fees = fees
    def StudentInfo(self):
        print('Student ID : {}'.format(self.studentid))
        print('Fees : {}'.format(self.fees))

class Teacher(Person):
    def __init__(self,name,age,gender,empid,salary):
        Person.__init__(self,name,age,gender)
        self.empid=empid
        self.salary = salary
    def TeacherInfo(self):
        print('Employee ID : {}'.format(self.empid))
        print('Salary: {}'.format(self.salary))

stud1 = Student('Anand',24,'Male',123456,12000)
print('STUDENT DETAILS')
print('----------------')
stud1.PersonInfo()
stud1.StudentInfo()
print()