
class Guest:
    def __init__(self, surname, name, phone, email, passport):
        self.surname = surname
        self.name = name
        self.phone = phone
        self.email = email
        self.passport = passport

    def __str__(self):
        return f"surname : {self.surname}, " \
               f"name : {self.name}, " \
               f"phone : {self.phone}, " \
               f"email : {self.email}, " \
               f"passport : {self.passport}"

    def search_guest_id(self, passport):
        if passport == self.passport:
            print(self.surname + " " + self.name, " ", "so happy to have you here again")
            return True
            # else:
            #     modules.new_guest(self.guest_list_c)
            #     return True

    # def getValue(self):
    #     return self.value

    def new_guest(self, d, guest_l):
        print('Please enter your personal information')
        # make check for details
        self.surname = input('Please enter your surname \n')
        self.name = input('Please enter your name \n')
        self.phone = input('Please enter your phone number \n')
        self.email = input('Please enter your email \n')
        self.passport = input('Please enter your ID/Passport number \n')
        # check function and check guest is not already in database
        # IF conditions
        d[self.passport] = self.surname, self.name, self.phone, self.email, self.passport
        guest_l.add_guest(d[self.passport])
        print(d[self.passport])
        return self , guest_l


class GuestList:
    def __init__(self):
        self.guest_list_c = []

    # def __repr__(self):
    #     return list(self)

    def add_guest(self, guest):
        self.guest_list_c.append(guest)

    # can't use because we can't access the data of the Guest object inside the dictionary or the list
    # def update_guest_info(self, passport):   #     for g in self.guest_list_c:
    #         if passport == g.passport:
    #             print(g.surname, g.name, g.phone, g.email)
    #             print('would you like to update your information?')


# add later :
# change surname, name, , phone, email
