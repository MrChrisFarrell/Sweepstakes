
def display_message(message):
    print(message)


def assign_contestant_info(last_used_registration_num=1):
    first_name = input("Enter contestant's first name - ")
    last_name = input("Enter contestant's last name - ")
    email = input("Enter contestant's email address - ")
    return [first_name, last_name, email, last_used_registration_num + 0]


def print_list_iterate(supplied_list):
    for thing in supplied_list:
        print(thing)


def get_input(message):
    result = input(message)
    return result


def verify(message):
    answer = input(message).lower()
    if answer == 'yes':
        return True
    else:
        return False
