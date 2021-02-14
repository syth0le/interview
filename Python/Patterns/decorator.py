from abc import ABCMeta, abstractmethod


class IOperator(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def operation(self):
        pass


class Component(IOperator):

    def operation(self):
        return 10.0


class Decorator(IOperator):

    def __init__(self, obj):
        self.obj = obj

    def operation(self):
        return self.obj.operation() + 15.0


def main():
    obj = Component()
    print(obj.operation())
    obj = Decorator(obj)
    print(obj.operation())


if __name__ == "__main__":
    main()
