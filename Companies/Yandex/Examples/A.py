# реализовать функции five, add, one, seven, subtract, two.
# five(add(one())) == 6 // true
# seven(subtract(two())) == 5 // true

def five(operator=None):
    if operator is None:
        return 5
    return operator(5)


def seven(operator=None):
    if operator is None:
        return 7
    return operator(7)


def one(operator=None):
    if operator is None:
        return 1
    return operator(1)


def two(operator=None):
    if operator is None:
        return 2
    return operator(2)


def add(val1):
    return lambda val2: val2 + val1


def subtract(val1):
    return lambda val2: val2 - val1


if __name__ == '__main__':
    print(five(add(one())))
    print(seven(subtract(two())))
