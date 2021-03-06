from user_interface import *


class Contestant:
    def __init__(self, first_name, last_name, email, registration_number):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.registration_number = registration_number
        self.is_winner = False

    def notify(self, is_winner):
        if is_winner:
            display_message(f"Congratulations {self.first_name} {self.last_name}!!!\nYou've won the sweepstakes!!!")
        else:
            display_message(f"Sorry {self.first_name} {self.last_name},\nYou did not win the sweepstakes!!!")