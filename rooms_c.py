class Room:
    def __init__(self, floor, number, category, bed, washroom, occupied, status,):
        self.floor = floor  # 1-4
        self.number = number  # room number
        self.category = category  # STD, STDT, SUP, SUPT
        self.bed = bed  # double or twin
        self.washroom = washroom  # bath or shower
        self.occupied = occupied  # true or false
        self.status = status  # meaning housekeeping status - clean, dirty, inspect

    def __str__(self):
        return f"floor : {self.floor}, " \
               f"number : {self.number}, " \
               f"category : {self.category}, " \
               f"bed : {self.bed}, " \
               f"washroom : {self.washroom}, " \
               f"occupancy : {self.occupied}, " \
               f"status : {self.status}"


class RoomList:
    def __init__(self):
        self.room_list_c = []

    def room_list(self, room):
        self.room_list_c.append(room)

    def availability(self):
        count = 0
        room_numbers = []
        for r in self.room_list_c:
            if r.occupied:  # == True
                count += 1
                room_numbers.append(r.number)
        if count == 0:
            print('We are sorry but currently we are fully booked. we will be happy to see you next time')
            return False
        print('The rooms that are available are', room_numbers)
        return True

    def clean_room_rep(self, list):
        for r in self.room_list_c:
            if r.status == 'Clean':
                print(r.number, ' | ', r.catergory, ' | ', r.bed, ' | ', r.washroom, ' | ')
