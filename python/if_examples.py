# Test by changing the age and/or gender and run the program multiple 
# times to see how the if tests are evaluated differently.

# Person 1:
person1_age = 30
person1_gender = "M"
# Person 2:
person2_age = 30
person2_gender = "K"

# (You can also change the content of the list and the dict on the botton, and see
# how that changes what is written out.)

# We want to run some code if the persons age are the same:
if person1_age == person2_age:
    print "The persons are the same age."
else:
    print "The persons are not the same age."

# We want to run some code if the persons age are the same, but in addition
# they have to be the same gender:
if person1_age == person2_age and person1_gender == person2_gender:
    print "The persons are the same age and the same gender."
else:
    print "Either, these persons are not the same age, or they are not the same gender."

# We want to run some code if the persons age are the same, or they 
# are the the same gender, they do not have to be both:
if person1_age == person2_age or person1_gender == person2_gender:
	print "The persons are the same age and the same gender."
else:
    print "Either, these persons are not the same age, or they are not the same gender."

# Add more if conditions to the same if
if person1_age == person2_age:
    print "The persons are the same age."
elif person1_age > person2_age:
    print "Person 1 is older than person 2."
elif person2_age > person1_age:
    print "Person 2 is older than person 1."
else:
    print "None of the above where true"


# Remember that we can choose to do something based on the content of a list:
example_list = [1, 2, 3]
if example_list:
    print "The list is not empty."

# And you can do the same with dictionaries
example_dict = {'a': 1, 'b': 2, 'c': 3}
if example_dict:
    print "The dictionary is not empty."





