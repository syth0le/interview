from typing import Generator


def generator():
    for i in range(20):
        yield i * i


def reversing(gen: Generator)-> Generator:
    return reversed((list(gen)))


if __name__ == "__main__":
    for elem in generator():
        print(elem)

    for elem in reversing(generator()):
        print(elem)