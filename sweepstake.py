import random
from publisher import Publisher
from subscriber import Subscriber
from user_interface import *


class Sweepstake:
    def __init__(self, name):
        self.name = name
        self.contestants = {}
        self.publisher = Publisher()

    """using dependency injection turning contestant into dictionary key/val and adding to dictionary"""
    def register_contestant(self, contestant):
        cont_dictionary = {
            f"{contestant.registration_number}": contestant
        }
        self.contestants.update(cont_dictionary)
        self.publisher.register(Subscriber(contestant))

    def pick_winner(self):
        winning_tuple = random.choice(list(self.contestants.items()))
        winner_key = winning_tuple[0]
        self.contestants[winner_key].is_winner = True
        for subscriber in self.publisher.subscribers:
            if subscriber.reg_num == int(winner_key):
                subscriber.is_winner = True

    def print_contestant_info_dict(self, contestant):
        display_message(contestant.first_name)
        display_message(contestant.last_name)
        display_message(contestant.email)
        display_message(contestant.registration_number)
