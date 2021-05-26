
def display_message(message):
    print(message)


def assign_contestant_info(last_used_registration_num=1):
    first_name = input("Enter first name - ")
    last_name = input("Enter last name - ")
    email = input("Enter email address - ")
    return [first_name, last_name, email, last_used_registration_num + 0]
