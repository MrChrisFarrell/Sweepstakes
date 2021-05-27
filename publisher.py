
class Publisher:
    def __init__(self):
        self.subscribers = set()

    def register(self, user):
        self.subscribers.add(user)

    def unregister(self, user):
        self.subscribers.discard(user)

    def dispatch(self):
        for subscriber in self.subscribers:
            if subscriber.is_winner:
                subscriber.update(f"Congratulations {subscriber.first_name} {subscriber.last_name}!!!\nYou've won the sweepstakes!!!")
            else:
                subscriber.update(f"Sorry {subscriber.first_name} {subscriber.last_name},\nYou did not win the sweepstakes")
