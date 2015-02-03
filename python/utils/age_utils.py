required_age_for_lisence = 18

def person_can_take_test_check(current_person_age):
    if current_person_age >= required_age_for_lisence:
        print "Person is", current_person_age, "and can take the test."
    else:
        print "Person cannot take the test yet! Age is", current_person_age

