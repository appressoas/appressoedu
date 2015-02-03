"""
We want to store name, email and study for many students.

This is step 1 in how we should do it to change the code in 
``class_motivation.py`` to a modern and useful program.
"""

# We have been thinking about it, and the we now classify the objects
# in the previous example as "students". Then it makes sense to create 
# a class "Student":

class Student:
    # We list the values we want
    name = None
    email = None
    study = None

    def write_out(self):
        print self.name
        print self.email
        print self.study

# Now we can start working with objects by using this class:

# We create an object for student 1
student1 = Student()
# We set the variables (often called attributes)
student1.name = "Jeffrey"
student1.email = "jeffrey@example.com"
student1.study = "Computer Science"

student2 = Student()
student2.name = "Walter"
student2.email = "walter@example.com"
student2.study = "Mathematics"

student3 = Student()
student3.name = "Donny"
student3.email = "donny@example.com"
student3.study = "Anthropology"

student4 = Student()
student4.name = "Jesus"
student4.email = "jesus@example.com"
student4.study = "Religion"

for student in [student1, student2, student3, student4]:
    student.write_out()
    print

# But: There are quite many lines of code here, and we want to make it prettier.
# Go on to class_example2.py

