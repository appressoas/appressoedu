# Example using a function that we created in the same file.

person1_age = 17
person2_age = 18
person3_age = 20

required_age_for_lisence = 18

def person_can_take_test_check(current_person_age):
    if current_person_age >= required_age_for_lisence:
        print "Person is", current_person_age, "and can take the test."
    else:
        print "Person cannot take the test yet! Age is", current_person_age

person_can_take_test_check(person1_age)
person_can_take_test_check(person2_age)
person_can_take_test_check(person3_age)

