from abc import ABCMeta, abstractmethod


class IHandler(metaclass=ABCMeta):
    """The Interface for handling requests."""

    @staticmethod
    @abstractmethod
    def set_successor(successor):
        """Set the next handler in the chain"""

    @staticmethod
    @abstractmethod
    def handle(amount):
        """Handle the event"""


class Handler50Euro(IHandler):
    """ConcreteHandler
    Dispense 50 euros notes if applicable,
    otherwise continue to successor
    """

    def __init__(self):
        self._successor = None

    def set_successor(self, successor):
        self._successor = successor

    def handle(self, amount):
        """Handle the dispensing of notes"""
        if amount >= 50:
            num = amount // 50
            remainder = amount % 50
            print(f"Dispensing {num} £50 note")
            if remainder != 0:
                self._successor.handle(remainder)
        else:
            self._successor.handle(amount)


class Handler20Euro(IHandler):
    """ConcreteHandler
    Dispense 20 euros notes if applicable,
    otherwise continue to successor
    """

    def __init__(self):
        self._successor = None

    def set_successor(self, successor):
        self._successor = successor

    def handle(self, amount):
        """Handle the dispensing of notes"""
        if amount >= 20:
            num = amount // 20
            remainder = amount % 20
            print(f"Dispensing {num} £20 note")
            if remainder != 0:
                self._successor.handle(remainder)
        else:
            self._successor.handle(amount)


class Handler10Euro(IHandler):
    """ConcreteHandler
    Dispense 10 euros notes if applicable,
    otherwise continue to successor
    """

    def __init__(self):
        self._successor = None

    def set_successor(self, successor):
        self._successor = successor

    def handle(self, amount):
        """Handle the dispensing of notes"""
        if amount >= 10:
            num = amount // 10
            remainder = amount % 10
            print(f"Dispensing {num} £10 note")
            if remainder != 0:
                self._successor.handle(remainder)
        else:
            self._successor.handle(amount)


class ATMChain:
    """The Chain Client"""

    def __init__(self):
        # initialize the successor chain
        self.chain1 = Handler50Euro()
        self.chain2 = Handler20Euro()
        self.chain3 = Handler10Euro()

        # set the chain of responsibility
        # The Client may compose chains once or
        # the hadler can set them dynamically at
        # handle time
        self.chain1.set_successor(self.chain2)
        self.chain2.set_successor(self.chain3)


if __name__ == "__main__":

    ATM = ATMChain()

    AMOUNT = int(input("Enter amount to withdrawal : "))
    if AMOUNT < 10 or AMOUNT % 10 != 0:
        print("Amount should be positive and in multiple of 10s.")
        exit()
    # process the request
    ATM.chain1.handle(AMOUNT)
    print("Now go spoil yourself")

