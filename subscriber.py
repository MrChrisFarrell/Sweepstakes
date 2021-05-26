from contestant import Contestant
from user_interface import *


class Subscriber:
    def __init__(self, contestant):
        self.first_name = contestant.first_name
        self.last_name = contestant.last_name
        self.email = contestant.email
        self.reg_num = contestant.registration_number
        self.is_winner = contestant.is_winner

    def update(self, message):
        display_message(message)
