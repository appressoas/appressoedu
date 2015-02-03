"""
Example for motivating using functions to group repeating code.

The check is; we print if a person is old enough to take his driver license.

We want to do some work with a persons age, so we store this
for 3 persons:
"""
person1_age = 17
person2_age = 18
person3_age = 20
required_age_for_lisence = 18

# Do the checks for person 1
if person1_age >= required_age_for_lisence:
    print "Person is", person1_age, "and can take the test."
else:
    print "Person cannot take the test yet! Age is", person1_age

# Do the checks for person 2
if person2_age >= required_age_for_lisence:
    print "Person is", person2_age, "and can take the test."
else:
    print "Person cannot take the test yet! Age is", person2_age

# Do the checks for person 3
if person3_age >= required_age_for_lisence:
    print "Person is", person3_age, "and can take the test."
else:
    print "Person cannot take the test yet! Age is", person3_age


