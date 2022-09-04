def main_menu():
    print('Welcome to Casa Del Gold-blat hotel. '
          '\n '  'We are delighted to see you.'
          '\n Please use the terminal in front of you to log in or register')  # credits for help
    c = input('Please select option : '
              '\n 1 - Register - New guest'
              '\n 2 - Log in - Existing guest'
              '\n 3 - staff'
              '\n Any key to exit'
              '\n :')
    return c


def staff_menu():
    c = input('Please select action :'
              '\n 1 - See availability'
              '\n 2 - Make reservation'
              '\n 3 - See clean rooms'
              '\n 4 - Change room status'
              '\n 5 - Check-in'
              '\n 6 - Check-out'
              '\n : ')
    return c


def availability(rooming_dict):
    count = 0
    for key in rooming_dict:
        if rooming_dict[key].status == "clean" and rooming_dict[key].occupied == "vacant":
            count += 1
    return count


def print_reservation(rooming_dict):
    for key in rooming_dict:
        if rooming_dict[key].status == "clean" and rooming_dict[key].occupied == "vacant":
            print(rooming_dict[key])
