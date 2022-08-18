# Start

from rooms_c import Room, RoomList
from guest_c import Guest, GuestList
from modules import new_guest, main_menu, staff_menu

rooms_l = RoomList()
room_report = []
room_dict = {}
guests_l = GuestList()
guest_report = []
guest_dict = {}


with open('room.list.txt', 'r') as room_file:
    room_file.readline()
    for line in room_file:
        room = line.split(",")
        r = Room(floor=str(room[0]),
                 number=str(room[1]),
                 category=str(room[2]),
                 bed=str(room[3]),
                 washroom=str(room[4]),
                 occupied=str(room[5]),
                 status=str(room[6]))
        room_report.append(r)
        room_dict[r.number] = r
        rooms_l.room_list(r)

with open('guest.list.txt', 'r') as guest_file:
    guest_file.readline()
    for line in guest_file:
        line = line.strip()
        guest = line.split(",")
        g = Guest(surname=str(guest[0]),
                  name=guest[1],
                  phone=guest[2],
                  email=guest[3],
                  passport=str(guest[4]))
        guest_report.append(g)
        guest_dict[g.passport] = g
        guests_l.add_guest(g)

gg = input("passport number:")
print(guest_dict[gg])

