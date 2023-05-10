from file1 import GreetingCard


class BirthdayCard(GreetingCard):
    def __init__(self, recipient="Dana Ev", sender="Eyal Ch", sender_age=0):
        super().__init__(recipient, sender)
        self._sender_age = sender_age

    def greeting_msg(self):
        print(f"Dear {self._recipient},\n\nHappy birthday from {self._sender} who is now {self._sender_age} years old!")
