# Start

from rooms_c import Room, RoomList
from guest_c import Guest, GuestList
from modules import main_menu, staff_menu

rooms_l = RoomList()
room_report = []
room_dict = {}
guests_l = GuestList()
guest_report = []
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
        room_report.append(r)
        room_dict[r.number] = r
        rooms_l.room_list(r)

with open('guest.list.txt', 'r') as guest_file:
    guest_file.readline()
    for line in guest_file:
        line = line.strip()
        guest = line.split(",")
        g = Guest(surname=guest[0],
                  name=guest[1],
                  phone=guest[2],
                  email=guest[3],
                  passport=guest[4])
        guest_report.append(g)
        guest_dict[g.passport] = g
        guests_l.add_guest(g)

print('Welcome to hotel Casa Del Gold-blat.') #credits for help

command = main_menu()

while command == '1' or command == '2' or command == '3':

    if command == '1':
        new = [g.new_guest(guest_dict, guests_l)] # gets new guest, save to dictionary doesn't work
        guest_dict[guests_l] = Guest(surname=new[0],
                                     name=new[1],
                                     phone=new[2],
                                     email=new[3],
                                     passport=new[4])

        print(guest_dict[g.passport]) #check
        print(g.name, g.surname,#check
              '\n welcome to our hotel, we hope you leave soon')
        command = '2'

    elif command == '2':
        while True:
            count = 3
            for key in guest_dict:
                passport = str(input('please enter your passport number'))
                if key == passport:
                    print('welcome back', guest_dict[key].name, guest_dict[key].surname)
                    action = input('Please select action :'
                                   '\n 1 - See availability'
                                   '\n 2 - Make reservation'
                                   '\n Back to main menu - press any key'
                                   '\n : ')
                else:
                    print("passport number doesn't match our database\n please try again")
                    count -= 1
                    if count == 0:
                        guest_dict = g.new_guest(guest_dict, guests_l) #still, doesnt saves to dictionary

            command = main_menu()


    elif command == '3':
        action = staff_menu()
        if action == '1':
            # function availability
        elif action == '2':
            # reservation
        elif action == '3':
            # see clean rooms
        elif action == '4':
             # change room status:
        elif action == '5':
            # check in
        elif action == '6':
            # check out
        command = main_menu()

    else:
        break

print('thank you for staying please dont come back ever again')
