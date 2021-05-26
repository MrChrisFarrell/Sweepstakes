from user_interface import *
from sweepstake import Sweepstake
from contestant import Contestant

"""Using dependency injection to make adding and removing sweepstakes"""
class MarketingFirm:
    def __init__(self, manager):
        self.manager = manager

    def create_sweepstakes(self):
        sweepstakes_name = get_input("Name the sweepstakes - ")
        sweepstakes = Sweepstake(sweepstakes_name)
        add_contestant = verify("Do you want to add a contestant? ")
        contestants_added = 0
        while add_contestant:
            contestant_info = assign_contestant_info(contestants_added)
            contestant = Contestant(contestant_info[0], contestant_info[1], contestant_info[2], contestant_info[3])
            sweepstakes.register_contestant(contestant)
            contestants_added += 1
            add_contestant = verify("Do you want to add another contestant? ")
        self.manager.insert_sweepstakes(sweepstakes)
