"""
We want to store name, email and study for many students.

This is step 2 in how we should do it to change the code in 
``class_motivation.py`` to a modern and useful program.
"""

# We have been thinking about it, and the we now classify the objects
# in the previous example as "students". Then it makes sense to create 
# a class "Student".
# But this is the same as in the example1, exept that we now use an 
# __init__ method.

class Student:

    def __init__(self, student_name, student_email, student_study):
        # We set the variables (often called attributes) here instead
        self.name = student_name
        self.email = student_email
        self.study = student_study

    def write_out(self):
        print self.name
        print self.email
        print self.study

# Now we can start working with objects by using this class:

# We create an object for student 1, and set the values we want
student1 = Student("Jeffrey", "jeffrey@example.com", "Computer Science")
student2 = Student("Walter", "walter@example.com", "Mathematics")
student3 = Student("Donny", "donny@example.com", "Anthropology")
student4 = Student("Jesus", "jesus@example.com", "Religion")

for student in [student1, student2, student3, student4]:
    student.write_out()
    print

