from abc import ABC, abstractmethod, ABCMeta


class IPrototype(metaclass=ABCMeta):
    @abstractmethod
    def clone(self):
        pass


class PrototypeClass1(IPrototype):
    def __init__(self, component='', number=0, array=[]):
        self.component = component
        self.number = number
        self.array = array

    def clone(self):
        return type(self)(
            self.component,
            self.number,
            self.array.copy())

    def __str__(self):
        return f"{self.component} {self.number} {self.array}"


class PrototypeClass2(IPrototype):
    def __init__(self, component='', number=0, array=[]):
        self.component = component
        self.number = number
        self.array = array

    def clone(self):
        return type(self)(
            self.component,
            self.number,
            self.array)

    def __str__(self):
        return f"{self.component} {self.number} {self.array}"


def main():
    obj1 = PrototypeClass1("class 1", 1, ['some1', 'some2', 'some3'])
    print(f'First object: {obj1}')

    obj2 = obj1.clone()
    print(f'Second object: {obj2}')

    obj2.array[0] = 'CHANGED_2'
    obj2.component = 'CHANGED_2'
    obj1.component = 'CHANGED_1'
    print(f'Second object: {obj2} type: {type(obj2)}')
    print(f'First object: {obj1} type: {type(obj1)}')


if __name__ == '__main__':
    main()
