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
        winning_key = key, val = random.choice(list(self.contestants.items()))
        winner = winning_key[val]
        return winner

    def print_contestant_info_dict(self, contestant_key):
        contestant = self.contestants.get(contestant_key)
        print_list_iterate(contestant)
