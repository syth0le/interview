from abc import ABC, abstractmethod


class Language:
    def __repr__(self):
        return self.__str__()


class Python(Language):
    def __str__(self):
        return 'Python'


class Swift(Language):
    def __str__(self):
        return 'Swift'


class Project(ABC):
    language = ''

    def __str__(self):
        return self.language.__str__()

    def __repr__(self):
        return self.language.__repr__()

    @abstractmethod
    def set_language(self):
        # можно и не делать его абстрактым, но эт делается для обеспечения реализации
        #         фабричного метода по умолчанию
        """Задать язык : это и есть наш Фабричный Метод"""
        raise AttributeError('Not Implemented Language')


class ProjectA(Project):
    def set_language(self):
        self.language = Python()


class ProjectB(Project):
    def set_language(self):
        self.language = Swift()


def main():
    project1 = ProjectA()
    project1.set_language()
    print(str(project1))

    project2 = ProjectB()
    project2.set_language()
    print(str(project2))

    if isinstance(project1, Project) & isinstance(project2, Project):
        print(True)

    # project3 = Project() # dont work for not implemented func in ancestor class
    # project3.set_language()
    # print(str(project3))


if __name__ == '__main__':
    main()
