"""
A program that handles student information. We
want to store name, email, study.
"""

class Person(object):
    name = ""
    email = ""

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def print_information(self):
        print "Name:", self.name
        print "Email:", self.email
        print

class Lecturer(Person):
    department = ""

    def __init__(self, name, email, department):
        self.department = department
        super(Lecturer, self).__init__(name, email)

class Student(Person):
    study = ""

lecturer = Lecturer("Tor", "tor@appresso.no", "Informatics")
print lecturer
lecturer.print_information()


