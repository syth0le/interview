def f(num: int):
    for i in range(num):
        yield i ** 3


if __name__ == "__main__":
    for x in f(5):
        print(x,)  # 0 1 8 27 64
