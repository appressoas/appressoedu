kvittr_messages = []
menu_index = 0

while menu_index != 9:
    print "1. Print all messages"
    print "2. Add new message"
    print "3. Delete a message"
    menu_index = input("What would you like to do?: ")

    if menu_index == 1:
        print kvittr_messages
    elif menu_index == 2:
        message = raw_input("Type in your message: ")
        kvittr_messages.append(message)
    elif menu_index == 3:
        for message_index in range(len(kvittr_messages)):
            print message_index, kvittr_messages[message_index]
        message_delete_index = input("Which message do you want to delete?: ")
        del kvittr_messages[message_delete_index]






