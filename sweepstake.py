
class Sweepstake:
    def __init__(self, name):
        self.name = name
        self.contestants = {}

    def register_contestant(self, contestant):
        cont_dictionary = {
            f"{contestant.registration_number}": contestant
        }
        self.contestants.update(cont_dictionary)
