# good structure of this class
class Room:
    def __init__(self, floor, number, category, bed, washroom, occupied, status,):
        self.floor = floor  # 1-4
        self.number = number  # room number
        self.category = category  # STD, STDT, SUP, SUPT
        self.bed = bed  # double or twin
        self.washroom = washroom  # bath or shower
        self.occupied = occupied  # vacant, occupied, reserved
        self.status = status  # meaning housekeeping status - clean, dirty, inspect

    def __str__(self):
        return f"floor : {self.floor}, " \
               f"number : {self.number}, " \
               f"category : {self.category}, " \
               f"bed : {self.bed}, " \
               f"washroom : {self.washroom}, " \
               f"occupancy : {self.occupied}, " \
               f"status : {self.status}"

    def reservation(self):
        self.occupied = input('Please room reservation status: '
                              '"vacant", "occupied", "reserved"\n')

    def housekeeping(self):
        # you are not checking what the user inputs. maybe it is better to check
        self.status = input('Please enter room status: '
                            '"clean", "dirty"\n')
    # improve the name - get_key maybe?
    # you double check clean and vacant - but that is ok.
    def check_key(self):
        if self.status == "clean" and self.occupied == "vacant":
            self.occupied = 'reserved'
            print('Room', self.number, 'is reserved for you. Have a nice day')
        else:
            print('an error has occurred, ask for help at the front desk')
        return

# this feature is not in use. it will be added with the next commit. 
# 5
# maybe you will want to see which guest is checking in - a refernece to guest class would be good here. maybe several guests per room?
# you need to think this over for the next step (database)
    def check_in(self):
        if self.status == "clean" and self.occupied == "reserved":
            self.occupied = 'occupied' 
            print('The guest is now checked in')
        else:
            print('The room you have selected is either dirty or not available. '
                  '\nPlease select a another room')
        return

# 6

    def check_out(self):
        self.occupied = 'vacant'
        self.status = 'dirty'
        print('The guest is now checked out, Please send cleaning crew')
