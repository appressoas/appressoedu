"""
We want to store name, email and study for student and lecturers.

This is another step in how we use object oriented programming to 
make a modern and useful program.
"""

class Student:
    def __init__(self, student_name, student_email, student_study):
        self.name = student_name
        self.email = student_email
        self.study = student_study

    def write_out(self):
        print self.name
        print self.email
        print self.study


# We also want to store information on lecturers.

class Lecturer:
    def __init__(self, lecturer_name, lecturer_email, lecturer_department):
        self.name = lecturer_name
        self.email = lecturer_email
        self.department = lecturer_department

    def write_out(self):
        print self.name
        print self.email
        print self.department

# Now we can start working with objects by using these classes:

student1 = Student("Jeffrey", "jeffrey@example.com", "Computer Science")
student2 = Student("Walter", "walter@example.com", "Mathematics")
student3 = Student("Donny", "donny@example.com", "Anthropology")
student4 = Student("Jesus", "jesus@example.com", "Religion")

for student in [student1, student2, student3, student4]:
    student.write_out()
    print

lecturer1 = Lecturer("Tor Ivar", "tor@example.com", "Computer Science")
lecturer2 = Lecturer("Magne", "magne@example.com", "Computer Science")
lecturer3 = Lecturer("Maude", "maude@example.com", "Mathematics")
lecturer4 = Lecturer("Bunny", "bunny@example.com", "Religion")

for lecturer in [lecturer1, lecturer2, lecturer3, lecturer4]:
    lecturer.write_out()
    print


