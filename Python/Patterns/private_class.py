"""
Control write access to class attributes.
Separate data from methods that use it.
Encapsulate class data initialization.
"""


class DataClass:
    """
    Hide all the attributes.
    """

    def __init__(self):
        self.value = None

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if self.value is None:
            self.value = value


class MainClass:
    """
    Initialize data class through the data class's constructor.
    """

    attribute = DataClass()

    def __init__(self, value):
        self.attribute = value


def main():
    m = MainClass(True)
    print(m.attribute)
    m.attribute = False
    print(m.attribute)
    # cant to assign THATS PRIVATE field.
    # we cant to rewrite data on private fields
    m = MainClass(False)
    print(m.attribute)


if __name__ == "__main__":
    main()
