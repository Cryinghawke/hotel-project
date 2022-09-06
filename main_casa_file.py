# Program base code infrastructure.

from rooms_c import Room
from guest_c import Guest
from modules import main_menu, staff_menu, availability, print_reservation

room_dict = {}
guest_dict = {}


with open('room.list.txt', 'r') as room_file:
    room_file.readline()
    for line in room_file:
        line = line.strip()
        room = line.split(",")
        r = Room(floor=room[0],
                 number=room[1],
                 category=room[2],
                 bed=room[3],
                 washroom=room[4],
                 occupied=room[5],
                 status=room[6])

        room_dict[r.number] = r


with open('guest.list.txt', 'r') as guest_file:
    guest_file.readline()
    for line in guest_file:
        line = line.strip()
        guest = line.split(",")

        # "g_file" - used for adding guest objects from database input

        g_file = Guest(surname=guest[0],
                       name=guest[1],
                       phone=guest[2],
                       email=guest[3],
                       passport=guest[4])
        guest_dict[g_file.passport] = g_file

# "g_user" - used for adding guest objects from user input
# note - when not using 2 different variables for creating a new guest object the new one entered overrides the last
# one from the file. (in the program itself, not the file)

g_user = Guest(surname=guest[0],
               name=guest[1],
               phone=guest[2],
               email=guest[3],
               passport=guest[4])

# Start Program


command = main_menu()

# as i said in class this is deeply nested code and not a good idea
# take a look here:
# https://wpshout.com/unconditionally-refactoring-nested-statements-cleaner-code/
while command == '1' or command == '2' or command == '3':

    if command == '1':  # new
        # this is hard to understand- the way you create a new guest. fix it. 
        # create it in a function. not in the class and return an Guest object.
        # then work with the object. what you do here is too complex
        surname, name, phone, email, guest_id = Guest.new_guest(g_user) 
        guest_dict[guest_id] = g_user
        # left for testing purposes ONLY do NOT use. # dont leave code if you dont need it
        # for key in guest_dict:
        #     print(guest_dict[key])
        command = '2'

    elif command == '2':
        # "tries" to limit endless loops trying to enter the right data
        tries = 3
        while tries != 0:
            passport = str(input('please enter your passport number to proceed\n'))
            if passport in guest_dict:
                tries = 0
                print('are your details correct? \n', guest_dict[passport])
                answer = str(input('"yes"  "no"\n'))
                if answer == 'yes':
                    print('welcome back', guest_dict[passport].name, guest_dict[passport].surname)
                    action = input('Please select action :'
                                   '\n 1 - See availability'
                                   '\n 2 - Make reservation'
                                   '\n Back to main menu - press any key'
                                   '\n : ')
                    if action == '1':
                        able = availability(room_dict)
                        if able == 0:
                            print('We regret to inform you we are currently fully booked '
                                  '\n Please check with us at a later date')
                        else:
                            print('There are', able, 'rooms available. '
                                  '\n Would you like to make a reservation?')
                            select = input('Please enter choice :  \n "yes" , "no"')
                            if select == "no":
                                print('You chose to not make a reservation. '
                                      '\n Do come again')
                                break
                            elif select == "yes":
                                print('Here are the available rooms \n')
                                print_reservation(room_dict) # modules
                                while True:
                                    number = input('Please select a room to reserve. '
                                                   '\nEnter room number: '
                                                   '\n')
                                    if number in room_dict.keys():
                                        Room.check_key(room_dict[number]) #better write room_dict[number].check_key()
                                        break
                                    print('choice is not valid, please choose again')
                    elif action == '2':
                        print('Here are the available rooms \n')
                        print_reservation(room_dict)  # modules
                        while True:
                            number = input('Please select a room to reserve. '
                                           '\nEnter room number: '
                                           '\n')
                            if number in room_dict.keys():
                                Room.check_key(room_dict[number])
                                break
                            print('choice is not valid, please choose again')

                elif answer == 'no':
                    # now i understand this is a way to update your details. 
                    # maybe it should be in main menu (but improve the nesting first)
                    Guest.update_guest(guest_dict[passport])
                    print('Thank you. \nYour details have been updated')
                    break
            else:
                tries -= 1
                print("passport number doesn't match our database\n please try again")
                if tries == 0:
                    print('You have exceeded the number or tries to log in.'
                          '\nPlease register a new account or speak with a staff member')
                    break
        command = main_menu()


# staff menu and option WIP not in use atm

    elif command == '3':
        action = staff_menu()
        if action == '1':
            able = availability(room_dict)
            if able == 0:
                print('There are no rooms available.')
            else:
                print('There are', able, 'rooms available')

        elif action == '2':
            print('# feature is currently unavailable. To be added in the next commit.')
        # # reservation

        # elif action == '3':
        # # see clean rooms

        elif action == '4':
            number = input('Please select a room to clean. '
                           '\nEnter room number: '
                           '\n')
            if number in room_dict.keys():
                Room.housekeeping(room_dict[number])
                break
            print('choice is not valid, please choose again')

        elif action == '5':
            print('# feature is currently unavailable. To be added in the next commit.')
        # Room.check_in()
        elif action == '6':
            print('# feature is currently unavailable. To be added in the next commit.')
        # # check out
        # command = main_menu()

    else:
        break
