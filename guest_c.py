
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

    def new_guest(self):
        print('Please enter your personal information')
        # make check for details
        self.surname = input('Please enter your surname \n')
        self.name = input('Please enter your name \n')
        self.phone = input('Please enter your phone number \n')
        self.email = input('Please enter your email \n')
        self.passport = input('Please enter your ID/Passport number \n')
        print('Welcome', self.name, self.surname,
              '\n You are now registered with us '
              '\n We hope you leave soon')
        return self.surname, self.name, self.phone, self.email, self.passport

    def update_guest(self):
        print('Please update your details')
        self.surname = input('Please enter your surname \n')
        self.name = input('Please enter your name \n')
        self.phone = input('Please enter your phone number \n')
        self.email = input('Please enter your email \n')
