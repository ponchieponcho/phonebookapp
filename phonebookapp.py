import os
d = {'Melissa':'584-394-5857', 'John':'404-312-1046'}
selection = 0
while selection != 5:
    print """
    Electronic Phone Book
    =====================
    1. Look up an entry
    2. Set an entry
    3. Delete an entry
    4. List all entries
    5. Quit
    """
    selection = int(raw_input("What do you want to do (1-5)?"))

    if selection == 2:
        input_name = raw_input('Name: ')
        input_phone_number = raw_input('Phone Number: ')
        d[input_name] = input_phone_number
        print ('Entry stored for %s.') % input_name

    elif selection == 1:
        input_name = raw_input('Name: ')
        printout_number = d[input_name]
        print 'Found entry for %s: %s' % (input_name,printout_number)

    elif selection == 3:
        input_name = raw_input('Who do you want to delete? ')
        del d[input_name]
        print 'Deleted entry for %s' % input_name

    elif selection == 4:
        for i in d:
            print 'Found entry for ' + i + ': ' + d[i]

print 'Bye.'
exit()