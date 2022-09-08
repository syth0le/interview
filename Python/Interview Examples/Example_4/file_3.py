# что будет если мы создадим объект Z? (Вопрос про MRO3)

class Base:
    def __init__(self):
        print('Base')


class X(Base):
    def __init__(self):
        super().__init__()
        print('X')


class Y(Base):
    def __init__(self):
        super().__init__()
        print('Y')


class Z(X, Y):
    def __init__(self):
        super().__init__()
        print('Z')


z_object = Z()