from abc import ABCMeta, abstractmethod
# На сайте два подхода композиционный и наследсвтенный  надо почекать что куда и как


class IA(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def method_a():
        pass


class IB(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def method_b():
        pass


class AComponent(IA):

    def method_a(self):
        print("String from class A")


class BComponent(IB):

    def method_b(self):
        print("String from class B")


class FromBtoAAdapter(IA):
    def __init__(self):
        self.class_b = BComponent()

    def method_a(self):
        """calls the class b method_b instead"""
        self.class_b.method_b()


def main():
    obj_a = AComponent()
    obj_b = BComponent()
    obj_a.method_a()
    obj_b.method_b()  # has no method_b, so we cant call it

    #using adapter
    obj_adaptered = FromBtoAAdapter()
    obj_adaptered.method_a()


if __name__ == "__main__":
    main()
