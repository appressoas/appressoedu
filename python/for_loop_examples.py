# Loops are something that we use to do something a given number of times.
# These are examples of using the python "for" loop.

print "Example 1:"
# Print a message 5 times.
# We use "range", which here will return numbers from 
# zero to 5, that is: 0, 1, 2, 3, 4. 
# Here we do not care what the numbers are, we just want
# to loop five times, and for every loop print a message:
for number in range(5):
    print "The message"

print "Example 2:"
# Print numbers counting from 1 to 5, with a "#" in front of it.
# Here we use range in another way than above. We need the first 
# number to be 1, we need the "step" (the increase) to be 1 per 
# loop, and we want the loop to stop when the current number is
# above 5 (5 was the last number we wanted to print). The 
# arguments to range are:
#   - number to start with
#   - number to stop at
#   - the number to increase with for every loop
for number in range(1, 6, 1):
    print "#", number

print "Example 3:"
# Print all elements in a list, with a "$" in front of it
example_list = [1, 2, 3, 4, 5]
for number in example_list:
    print "$", number

print "Example 4:"
# Print all elements in a dictionary.
# Remember that elements in a dictionary with pairs of a key and a value.
# We create a test dictionary where the account number is used as key (we
# suppose that account number is unique) and the value we want is company 
# name.
accounts = {
    '642112': "Appresso AS",
    '234671': "University of Halden",
    '552125': "Telesnor AS",
}
for account_number, company_name in accounts.iteritems():
    print "Account with number", account_number, "is owned by company", company_name

print "Example 5"
# Print all elements in dictionary.
# This is the same as in example 4, but here we do it without using the "iteritems"
# function. What happens here, is that for each loop you get the key. To get the value
# in this case, you need to do it like shown here:
for account_number in accounts:
    print "Account with number", account_number, "is owned by company", accounts[account_number]



