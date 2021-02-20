from abc import ABCMeta, abstractmethod


class IObserver(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def notify(observable, *args, **kwargs):
        pass


class Observer(IObserver):

    def __init__(self, observable):
        observable.subscribe(self)

    def notify(self, observable, *args, **kwargs):
        print("Observer received", args, kwargs)


class IObservable(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def subscribe(observer):
        """The subscribe method"""

    @staticmethod
    @abstractmethod
    def unsubscribe(observer):
        """The unsubscribe method"""

    @staticmethod
    @abstractmethod
    def notify(observer):
        """The notify method"""


class Subject(IObservable):
    def __init__(self):
        self._observers = set()

    def subscribe(self, observer):
        self._observers.add(observer)

    def unsubscribe(self, observer):
        self._observers.remove(observer)

    def notify(self, *args, **kwargs):
        for observer in self._observers:
            observer.notify(self, *args, **kwargs)


def main():
    SUBJECT = Subject()
    observer_a = Observer(SUBJECT)
    observer_b = Observer(SUBJECT)  # firstly was 2 subscribers then 1 was removed

    SUBJECT.notify("Hello Observers")
    SUBJECT.subscribe(observer_b)
    SUBJECT.unsubscribe(observer_b)
    print()
    SUBJECT.notify("Hello Observers")  # last subscriber get notification


if __name__ == '__main__':
    main()
