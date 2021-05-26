from queue import Queue


class SweepstakesQueueManager:
    def __init__(self):
        self.queue = Queue()

    def insert_sweepstakes(self, sweepstake):
        self.queue.enqueue(sweepstake)

    def get_sweepstakes(self):
        self.queue.dequeue()
