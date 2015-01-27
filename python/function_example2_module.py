from utils.age_utils import person_can_take_test_check

# Some comments for new python programmers:
# What happens in the first line?
# We say that in a file or directory named "utils", there should be 
# a file or directory called "age_utils".
# 
# In our case "utils" is a directory, and because there exists a file 
# "__init__.py" in this directory, Python will make it usable for us.
# 
# "age_utils" is a file, and in this file we want to make the function
# person_can_take_test_check available to us.

person1_age = 17
person2_age = 18
person3_age = 20

person_can_take_test_check(person1_age)
person_can_take_test_check(person2_age)
person_can_take_test_check(person3_age)

# Of course, we can also send numbers as argument:
person_can_take_test_check(72)
