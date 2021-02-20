from abc import ABCMeta, abstractmethod


class Unit(metaclass=ABCMeta):
    """
    Абстрактный компонент, в данном случае это - отряд (отряд может
    состоять из одного солдата или более)
    """

    @abstractmethod
    def print(self) -> None:
        pass


class Legolas(Unit):

    def print(self) -> None:
        print('Леголас', end=' ')


class Aragorn(Unit):

    def print(self) -> None:
        print('Арагорн', end=' ')


class Gimli(Unit):

    def print(self) -> None:
        print('Гимли', end=' ')


class Boromir(Unit):

    def print(self) -> None:
        print('Боромир', end=' ')


class Hobbit(Unit):

    def print(self) -> None:
        print('Хоббит', end=' ')


class RingSquad(Unit):
    """
        Компоновщик - отряд, состоящий более чем из одного человека. Также
        может включать в себя другие отряды-компоновщики.
        """

    def __init__(self):
        self._units = []

    def print(self) -> None:
        print("Отряд {} (".format(self.__hash__()), end=' ')
        for u in self._units:
            u.print()
        print(')')

    def add(self, unit: Unit) -> None:
        """
        Добавление нового отряда

        :param unit: отряд (может быть как базовым, так и компоновщиком)
        """
        self._units.append(unit)
        unit.print()
        print('присоединился к отряду {}'.format(self.__hash__()))
        print()

    def remove(self, unit: Unit) -> None:
        """
        Удаление отряда из текущего компоновщика

        :param unit: объект отряда
        """
        for u in self._units:
            if u == unit:
                self._units.remove(u)
                u.print()
                print('покинул отряд {}'.format(self.__hash__()))
                print()
                break
        else:
            unit.print()
            print('в отряде {} не найден'.format(self.__hash__()))
            print()


if __name__ == '__main__':
    print('OUTPUT:')
    squad = RingSquad()
    squad.add(Aragorn())
    squad.add(Legolas())
    squad.add(Gimli())
    boromir = Boromir()
    squad.add(boromir)
    squad.remove(boromir)
    squad.print()
    squad_big = RingSquad()
    squad_big.add(Hobbit())
    squad_big.add(Hobbit())
    squad_big.add(squad)
    squad_big.print()
