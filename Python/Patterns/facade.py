class SubClassA:
    @staticmethod
    def method():
        return "A"


class SubClassB:
    @staticmethod
    def method():
        return "B"


class SubClassC:
    @staticmethod
    def method():
        return "C"


# facade
class Facade:
    def __init__(self):
        self.sub_class_a = SubClassA()
        self.sub_class_b = SubClassB()
        self.sub_class_c = SubClassC()

    def create(self):
        result = self.sub_class_a.method()
        result += self.sub_class_b.method()
        result += self.sub_class_c.method()
        return result


def main():
    FACADE = Facade()
    RESULT = FACADE.create()
    print("The Result = %s" % RESULT)


if __name__ == '__main__':
    main()