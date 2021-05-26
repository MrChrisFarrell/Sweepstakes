from stack import Stack


class SweepstakesStackManager:
    def __init__(self):
        self.stack = Stack()

    def insert_sweepstakes(self, sweepstake):
        self.stack.push(sweepstake)

    def get_sweepstakes(self):
        self.stack.pop()
