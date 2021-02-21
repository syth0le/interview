from abc import ABCMeta, abstractmethod


class MakeMeal(metaclass=ABCMeta):

    @abstractmethod
    def prepare(self): pass

    @abstractmethod
    def cook(self): pass

    @abstractmethod
    def eat(self): pass

    def template_method(self):
        self.prepare()
        self.cook()
        self.eat()


class MakePizza(MakeMeal):
    def prepare(self):
        print("Prepare Pizza")

    def cook(self):
        print("Cook Pizza")

    def eat(self):
        print("Eat Pizza")


class MakeTea(MakeMeal):
    def prepare(self):
        print("Prepare Tea")

    def cook(self):
        print("Cook Tea")

    def eat(self):
        print("Eat Tea")


class MakeSweets(MakeMeal):
    def prepare(self):
        print("Prepare Sweets")

    def cook(self):
        print("Cook Sweets")

    def eat(self):
        print("Eat Sweets")


def main():
    makePizza = MakePizza()
    makePizza.template_method()
    print()

    makeTea = MakeTea()
    makeTea.template_method()
    print()

    makeSweets = MakeSweets()
    makeSweets.template_method()


if __name__ == "__main__":
    main()
